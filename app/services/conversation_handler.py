import structlog
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import User, GiftSession
from app.services.ai_service import AIService

logger = structlog.get_logger()


class ConversationHandler:
    """Handles conversation flow and context management"""
    
    def __init__(self):
        self.ai_service = AIService()
    
    async def process_message(self, user_id: str, message: str, platform: str) -> str:
        """Process an incoming message and return a response"""
        
        try:
            # Get or create user
            async for db in get_db():
                user = await self.get_or_create_user(db, user_id, platform)
                
                # Get or create active session
                session = await self.get_or_create_session(db, user, platform)
                
                # Update user activity
                user.add_conversation()
                
                # Process message based on conversation state
                response = await self.generate_response(db, user, session, message)
                
                # Store conversation turn
                session.add_conversation_turn(message, response)
                
                # Commit changes
                await db.commit()
                
                logger.info(
                    "Message processed successfully",
                    user_id=user_id,
                    session_id=str(session.id),
                    platform=platform
                )
                
                return response
        
        except Exception as e:
            logger.error("Error processing message", exc_info=e, user_id=user_id)
            return "I'm sorry, I'm having trouble understanding. Could you try rephrasing that? 🤖"
    
    async def get_or_create_user(self, db: AsyncSession, user_id: str, platform: str) -> User:
        """Get existing user or create new one"""
        
        # Query for existing user based on platform
        if platform == "instagram":
            result = await db.execute(
                select(User).where(User.instagram_id == user_id)
            )
        elif platform == "whatsapp":
            result = await db.execute(
                select(User).where(User.whatsapp_id == user_id)
            )
        else:
            raise ValueError(f"Unsupported platform: {platform}")
        
        user = result.scalar_one_or_none()
        
        if user is None:
            # Create new user
            user_data = {}
            if platform == "instagram":
                user_data["instagram_id"] = user_id
            elif platform == "whatsapp":
                user_data["whatsapp_id"] = user_id
            
            user = User(**user_data)
            db.add(user)
            await db.flush()  # Get the ID
            
            logger.info("New user created", user_id=user_id, platform=platform, db_id=str(user.id))
        
        return user
    
    async def get_or_create_session(self, db: AsyncSession, user: User, platform: str) -> GiftSession:
        """Get active session or create new one"""
        
        # Look for active session
        result = await db.execute(
            select(GiftSession).where(
                GiftSession.user_id == user.id,
                GiftSession.status == "active"
            ).order_by(GiftSession.created_at.desc())
        )
        
        session = result.scalar_one_or_none()
        
        if session is None:
            # Create new session
            session = GiftSession(
                user_id=user.id,
                platform=platform
            )
            db.add(session)
            await db.flush()  # Get the ID
            
            logger.info("New gift session created", user_id=str(user.id), session_id=str(session.id))
        
        return session
    
    async def generate_response(self, db: AsyncSession, user: User, session: GiftSession, message: str) -> str:
        """Generate appropriate response based on conversation state"""
        
        # Determine conversation stage
        conversation_turns = len(session.conversation_context.get("turns", []))
        
        # First interaction - greeting and introduction
        if conversation_turns == 0:
            return await self.handle_greeting(user, session, message)
        
        # Early conversation - gather context
        elif conversation_turns < 3:
            return await self.handle_context_gathering(user, session, message)
        
        # Ready for recommendations
        elif self.has_enough_context(session):
            return await self.handle_recommendation_request(user, session, message)
        
        # Continue gathering context
        else:
            return await self.handle_context_gathering(user, session, message)
    
    async def handle_greeting(self, user: User, session: GiftSession, message: str) -> str:
        """Handle first interaction with user"""
        
        # Check if user has a name we can use
        greeting_name = user.name or "there"
        
        # Returning user vs new user
        if user.total_conversations > 1:
            return f"Welcome back, {greeting_name}! 👋 I'm here to help you find the perfect gift again. What's the occasion this time?"
        else:
            return (
                f"Hi {greeting_name}! 👋 I'm your AI gift advisor. I help people find thoughtful, "
                f"meaningful gifts by understanding the relationship and occasion.\n\n"
                f"Who are you shopping for and what's the occasion? 🎁"
            )
    
    async def handle_context_gathering(self, user: User, session: GiftSession, message: str) -> str:
        """Gather context about the gift recipient and occasion"""
        
        # Use AI to extract context and ask smart follow-up questions
        context_response = await self.ai_service.extract_context_and_respond(
            message=message,
            session_context=session.conversation_context,
            user_preferences=user.preferences
        )
        
        # Update session with extracted insights
        if context_response.get("extracted_insights"):
            session.update_insights(context_response["extracted_insights"])
        
        return context_response.get("response", "Could you tell me more about what you're looking for?")
    
    async def handle_recommendation_request(self, user: User, session: GiftSession, message: str) -> str:
        """Generate gift recommendations"""
        
        try:
            # Generate recommendations using AI
            recommendations = await self.ai_service.generate_recommendations(
                session_context=session.conversation_context,
                extracted_insights=session.extracted_insights,
                user_preferences=user.preferences,
                budget_range=(session.budget_min, session.budget_max)
            )
            
            # Store recommendations in session
            session.add_recommendations(recommendations.get("recommendations", []))
            
            # Format response
            return self.format_recommendations_response(recommendations)
        
        except Exception as e:
            logger.error("Error generating recommendations", exc_info=e, session_id=str(session.id))
            return "I'm having trouble generating recommendations right now. Could you tell me a bit more about what you're looking for?"
    
    def has_enough_context(self, session: GiftSession) -> bool:
        """Check if we have enough context to make recommendations"""
        
        insights = session.extracted_insights or {}
        
        # Basic requirements
        has_recipient = bool(insights.get("recipient_type") or session.recipient_name)
        has_occasion = bool(insights.get("occasion") or session.occasion)
        
        # Either explicit budget or enough context to infer
        has_budget_context = (
            session.budget_min is not None or 
            session.budget_max is not None or
            insights.get("budget_hints")
        )
        
        return has_recipient and has_occasion and len(session.conversation_context.get("turns", [])) >= 2
    
    def format_recommendations_response(self, recommendations: dict) -> str:
        """Format AI recommendations into user-friendly response"""
        
        if not recommendations.get("recommendations"):
            return "I'm having trouble finding good matches. Could you give me a bit more detail about their interests?"
        
        response = "Here are some thoughtful gift ideas I found for you:\n\n"
        
        for i, rec in enumerate(recommendations["recommendations"][:3], 1):
            response += f"{i}. **{rec.get('name', 'Gift idea')}**\n"
            response += f"   {rec.get('description', '')}\n"
            if rec.get('reasoning'):
                response += f"   💡 Why this works: {rec['reasoning']}\n"
            if rec.get('estimated_price'):
                response += f"   💰 Around ${rec['estimated_price']}\n"
            response += "\n"
        
        response += "Which of these resonates with you? Or would you like me to explore different directions? 🎁"
        
        return response