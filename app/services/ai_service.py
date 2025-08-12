import structlog
from typing import Dict, List, Optional, Tuple, Any
from openai import AsyncOpenAI
import json

from app.config import get_settings

logger = structlog.get_logger()


class AIService:
    """Service for AI-powered gift recommendations and conversation handling"""
    
    def __init__(self):
        settings = get_settings()
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        self.model = "gpt-4-turbo"
    
    async def extract_context_and_respond(
        self, 
        message: str, 
        session_context: Dict, 
        user_preferences: Dict
    ) -> Dict[str, Any]:
        """Extract context from user message and generate appropriate follow-up response"""
        
        conversation_history = self._format_conversation_history(session_context)
        
        system_prompt = """You are a thoughtful gift advisor AI. Your goal is to understand the gift recipient and occasion through natural conversation.

CONTEXT EXTRACTION: Analyze each message to extract:
- recipient_type: relationship (mom, friend, colleague, etc.)
- recipient_age_range: if mentioned or inferable
- occasion: birthday, anniversary, apology, holiday, etc.
- interests: hobbies, preferences, lifestyle
- personality_traits: outgoing, introverted, practical, creative, etc.
- budget_hints: any price mentions or budget clues
- emotional_context: celebration, apology, gratitude, etc.

RESPONSE STRATEGY: Ask ONE smart follow-up question that:
- Builds on what they just shared
- Gathers the most important missing information
- Feels natural and conversational
- Avoids overwhelming them

TONE: Warm, helpful, and genuinely interested in finding the perfect gift."""

        user_prompt = f"""
Current conversation:
{conversation_history}

Latest message: "{message}"

Previous context extracted: {session_context.get('extracted_insights', {})}

Extract new insights and provide a natural follow-up response that gathers one key piece of missing information.

Respond in JSON format:
{{
    "extracted_insights": {{
        "recipient_type": "string or null",
        "occasion": "string or null", 
        "interests": ["list of interests"],
        "budget_hints": "string or null",
        "emotional_context": "string or null"
    }},
    "response": "your follow-up question/response"
}}"""

        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            # Parse JSON response
            result = json.loads(response.choices[0].message.content)
            
            logger.info(
                "Context extracted successfully",
                extracted_insights=result.get("extracted_insights", {})
            )
            
            return result
        
        except Exception as e:
            logger.error("Error extracting context", exc_info=e)
            
            # Fallback response
            return {
                "extracted_insights": {},
                "response": "That's helpful! Could you tell me a bit more about them - what do they enjoy doing in their free time?"
            }
    
    async def generate_recommendations(
        self,
        session_context: Dict,
        extracted_insights: Dict,
        user_preferences: Dict,
        budget_range: Tuple[Optional[int], Optional[int]] = (None, None)
    ) -> Dict[str, Any]:
        """Generate personalized gift recommendations"""
        
        conversation_history = self._format_conversation_history(session_context)
        
        # Prepare context for AI
        context_summary = self._summarize_context(extracted_insights, conversation_history)
        budget_info = self._format_budget_info(budget_range, extracted_insights)
        
        system_prompt = """You are an expert gift advisor with deep understanding of human relationships and thoughtful gift-giving.

Your task is to recommend 3-5 specific, thoughtful gifts based on the conversation context.

RECOMMENDATION CRITERIA:
- Thoughtful and personal (not generic)
- Appropriate for the relationship and occasion
- Match the recipient's interests and personality
- Consider the emotional context
- Respect budget constraints
- Explain WHY each gift works

AVOID:
- Generic gifts (gift cards, flowers, chocolate boxes)
- Items requiring extensive knowledge of specific preferences (clothing sizes, exact tech specs)
- Overly expensive items without clear value justification

For each recommendation, provide:
- name: Clear, specific gift name
- description: 1-2 sentence description
- reasoning: Why this gift matches the recipient and occasion
- estimated_price: Reasonable price estimate
- where_to_find: General guidance (online, local stores, specific retailers)"""

        user_prompt = f"""
CONTEXT SUMMARY:
{context_summary}

BUDGET: {budget_info}

USER PREFERENCES: {user_preferences}

Generate 3-5 thoughtful gift recommendations in JSON format:
{{
    "recommendations": [
        {{
            "name": "Specific gift name",
            "description": "Brief description",
            "reasoning": "Why this works for this person/occasion",
            "estimated_price": 25,
            "where_to_find": "Where to buy guidance"
        }}
    ],
    "explanation": "Brief explanation of your approach"
}}"""

        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.8,
                max_tokens=1000
            )
            
            # Parse JSON response
            result = json.loads(response.choices[0].message.content)
            
            logger.info(
                "Recommendations generated successfully",
                num_recommendations=len(result.get("recommendations", []))
            )
            
            return result
        
        except Exception as e:
            logger.error("Error generating recommendations", exc_info=e)
            
            # Fallback recommendations
            return {
                "recommendations": [
                    {
                        "name": "Personalized photo book",
                        "description": "A custom photo book with shared memories",
                        "reasoning": "Personal and meaningful for any relationship",
                        "estimated_price": 25,
                        "where_to_find": "Online photo services like Shutterfly"
                    }
                ],
                "explanation": "Fallback recommendation due to processing error"
            }
    
    def _format_conversation_history(self, session_context: Dict) -> str:
        """Format conversation history for AI context"""
        turns = session_context.get("turns", [])
        
        if not turns:
            return "No previous conversation"
        
        history = []
        for turn in turns[-5:]:  # Last 5 turns to stay within token limits
            history.append(f"User: {turn.get('user_message', '')}")
            history.append(f"Assistant: {turn.get('bot_response', '')}")
        
        return "\n".join(history)
    
    def _summarize_context(self, extracted_insights: Dict, conversation_history: str) -> str:
        """Create a context summary for recommendation generation"""
        
        summary_parts = []
        
        # Recipient info
        if extracted_insights.get("recipient_type"):
            summary_parts.append(f"Recipient: {extracted_insights['recipient_type']}")
        
        if extracted_insights.get("occasion"):
            summary_parts.append(f"Occasion: {extracted_insights['occasion']}")
        
        if extracted_insights.get("interests"):
            interests = ", ".join(extracted_insights["interests"])
            summary_parts.append(f"Interests: {interests}")
        
        if extracted_insights.get("emotional_context"):
            summary_parts.append(f"Emotional context: {extracted_insights['emotional_context']}")
        
        # Add conversation snippet
        if conversation_history and conversation_history != "No previous conversation":
            summary_parts.append(f"Recent conversation:\n{conversation_history}")
        
        return "\n".join(summary_parts) if summary_parts else "Limited context available"
    
    def _format_budget_info(self, budget_range: Tuple[Optional[int], Optional[int]], extracted_insights: Dict) -> str:
        """Format budget information for AI"""
        
        budget_min, budget_max = budget_range
        
        if budget_min and budget_max:
            return f"${budget_min} - ${budget_max}"
        elif budget_max:
            return f"Under ${budget_max}"
        elif budget_min:
            return f"At least ${budget_min}"
        elif extracted_insights.get("budget_hints"):
            return f"Budget hints: {extracted_insights['budget_hints']}"
        else:
            return "No specific budget mentioned - suggest range of options"