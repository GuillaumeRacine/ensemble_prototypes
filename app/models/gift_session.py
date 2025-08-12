from sqlalchemy import Column, String, DateTime, Integer, Text, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum
import uuid

from app.database import Base


class SessionStatus(str, Enum):
    """Gift session status options"""
    ACTIVE = "active"
    COMPLETED = "completed"
    ABANDONED = "abandoned"


class GiftSession(Base):
    """Gift session model for tracking individual gift-seeking conversations"""
    
    __tablename__ = "gift_sessions"
    
    # Primary key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Foreign key to user
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    
    # Session metadata
    status = Column(String(20), default=SessionStatus.ACTIVE.value)
    platform = Column(String(20), nullable=False)  # instagram, whatsapp, etc.
    
    # Gift context
    recipient_name = Column(String(100), nullable=True)
    relationship_type = Column(String(50), nullable=True)  # mom, friend, colleague, etc.
    occasion = Column(String(100), nullable=True)
    
    # Budget constraints
    budget_min = Column(Integer, nullable=True)
    budget_max = Column(Integer, nullable=True)
    
    # Emotional context
    primary_emotion = Column(String(50), nullable=True)  # celebration, apology, gratitude, etc.
    relationship_goal = Column(String(100), nullable=True)  # strengthen_bond, show_appreciation, etc.
    
    # Rich context (stored as JSON)
    conversation_context = Column(JSON, default=dict)  # Full conversation history
    extracted_insights = Column(JSON, default=dict)   # AI-extracted insights about recipient
    user_constraints = Column(JSON, default=dict)     # Dietary restrictions, shipping constraints, etc.
    
    # Recommendations and outcomes
    recommendations_given = Column(JSON, default=list)
    user_feedback = Column(JSON, default=dict)
    final_choice = Column(String(500), nullable=True)
    satisfaction_score = Column(Integer, nullable=True)  # 1-5 rating
    
    # Timing
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationship
    user = relationship("User", back_populates="gift_sessions")
    
    def __repr__(self):
        return f"<GiftSession(id={self.id}, user_id={self.user_id}, status={self.status})>"
    
    def add_conversation_turn(self, user_message: str, bot_response: str):
        """Add a conversation turn to the session"""
        if self.conversation_context is None:
            self.conversation_context = {"turns": []}
        
        turn = {
            "timestamp": func.now().isoformat(),
            "user_message": user_message,
            "bot_response": bot_response
        }
        self.conversation_context["turns"].append(turn)
    
    def update_insights(self, new_insights: dict):
        """Update extracted insights about the recipient"""
        if self.extracted_insights is None:
            self.extracted_insights = {}
        self.extracted_insights.update(new_insights)
    
    def add_recommendations(self, recommendations: list):
        """Store the recommendations given to the user"""
        if self.recommendations_given is None:
            self.recommendations_given = []
        self.recommendations_given.extend(recommendations)
    
    def complete_session(self, final_choice: str = None, satisfaction: int = None):
        """Mark session as completed"""
        self.status = SessionStatus.COMPLETED.value
        self.completed_at = func.now()
        if final_choice:
            self.final_choice = final_choice
        if satisfaction:
            self.satisfaction_score = satisfaction
    
    def abandon_session(self):
        """Mark session as abandoned"""
        self.status = SessionStatus.ABANDONED.value
        self.completed_at = func.now()


# Add the relationship to User model
from app.models.user import User
User.gift_sessions = relationship("GiftSession", back_populates="user")