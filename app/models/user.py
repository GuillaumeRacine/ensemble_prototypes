from sqlalchemy import Column, String, DateTime, Integer, Text, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.database import Base


class User(Base):
    """User model for Present Agent users"""
    
    __tablename__ = "users"
    
    # Primary key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Platform-specific identifiers
    instagram_id = Column(String(255), unique=True, nullable=True, index=True)
    whatsapp_id = Column(String(255), unique=True, nullable=True, index=True)
    
    # Basic profile
    name = Column(String(100), nullable=True)
    email = Column(String(255), unique=True, nullable=True)
    
    # Preferences and context (stored as JSON)
    preferences = Column(JSON, default=dict)
    personality_traits = Column(JSON, default=dict)
    values = Column(JSON, default=dict)  # e.g., {"sustainability": True, "local_business": True}
    
    # Gift-giving patterns
    typical_budget_min = Column(Integer, nullable=True)
    typical_budget_max = Column(Integer, nullable=True)
    planning_style = Column(String(50), nullable=True)  # spontaneous, planner, mixed
    
    # Activity tracking
    total_conversations = Column(Integer, default=0)
    successful_recommendations = Column(Integer, default=0)
    last_active = Column(DateTime(timezone=True), nullable=True)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, instagram_id={self.instagram_id})>"
    
    @property
    def platform_id(self) -> str:
        """Get the primary platform ID for this user"""
        return self.instagram_id or self.whatsapp_id or str(self.id)
    
    def update_preferences(self, new_preferences: dict):
        """Update user preferences, merging with existing ones"""
        if self.preferences is None:
            self.preferences = {}
        self.preferences.update(new_preferences)
    
    def add_conversation(self):
        """Increment conversation count"""
        self.total_conversations = (self.total_conversations or 0) + 1
    
    def add_successful_recommendation(self):
        """Increment successful recommendation count"""
        self.successful_recommendations = (self.successful_recommendations or 0) + 1