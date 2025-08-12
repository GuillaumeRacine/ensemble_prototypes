# Present Agent: Optimal Data Model Architecture

## **Core Philosophy: The Relationship-Centric Model**

Present Agent's data model is designed around **relationships, not transactions**. Every piece of data serves to understand and enhance human connections through gifting.

## **1. Multi-Database Architecture**

```python
class DataModelStrategy:
    """Hybrid approach using specialized databases for different data types"""
    
    databases = {
        "postgresql": "Transactional data, user accounts, sessions",
        "neo4j": "Relationship graph, social connections, influence patterns", 
        "vector_db": "Semantic embeddings, gift matching, cultural intelligence",
        "redis": "Real-time state, conversation context, hot data",
        "event_store": "Behavioral history, learning patterns, audit trail"
    }
```

## **2. PostgreSQL: Core Transactional Schema**

```sql
-- === USERS & AUTHENTICATION ===
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    name VARCHAR(100) NOT NULL,
    
    -- Subscription & Status
    subscription_tier VARCHAR(20) DEFAULT 'free', -- free, premium, enterprise
    account_status VARCHAR(20) DEFAULT 'active',
    
    -- Onboarding & Engagement
    onboarding_completed_at TIMESTAMP,
    last_active_at TIMESTAMP NOT NULL DEFAULT NOW(),
    conversation_count INTEGER DEFAULT 0,
    
    -- Demographics (for cultural intelligence)
    birth_year INTEGER,
    location_country VARCHAR(2), -- ISO country code
    location_city VARCHAR(100),
    timezone VARCHAR(50),
    languages TEXT[], -- Array of language codes
    cultural_background TEXT[], -- Self-identified cultures
    
    -- Metadata
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- === RECIPIENTS (People you give gifts to) ===
CREATE TABLE recipients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Identity
    name VARCHAR(100) NOT NULL,
    real_name VARCHAR(100), -- Full legal name if different
    nickname VARCHAR(50),
    
    -- Relationship Context
    relationship_type VARCHAR(50) NOT NULL, -- family, friend, romantic, colleague, etc.
    relationship_label VARCHAR(100), -- "mom", "best friend", "coworker"
    relationship_since DATE,
    importance_level INTEGER CHECK (importance_level BETWEEN 1 AND 10),
    
    -- Demographics
    approximate_age INTEGER,
    gender VARCHAR(20),
    location VARCHAR(100),
    
    -- Communication Patterns
    communication_frequency VARCHAR(20), -- daily, weekly, monthly, rarely
    preferred_contact_method VARCHAR(20), -- text, call, email, in_person
    last_contact_date DATE,
    
    -- Gift Context
    total_gifts_given INTEGER DEFAULT 0,
    last_gift_occasion VARCHAR(100),
    last_gift_date DATE,
    average_gift_budget DECIMAL(10,2),
    
    -- Rich Profile Data (JSON for flexibility)
    personality_traits JSONB, -- Big 5, interests, quirks
    preferences JSONB, -- likes, dislikes, allergies, values
    life_context JSONB, -- job, family status, recent events
    gift_history_summary JSONB, -- successful patterns, failures
    
    -- Metadata
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    
    -- Unique constraint
    UNIQUE(user_id, name)
);

-- === GIFT SESSIONS (Each gift-seeking conversation) ===
CREATE TABLE gift_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    recipient_id UUID REFERENCES recipients(id) ON DELETE SET NULL,
    
    -- Session Context
    session_status VARCHAR(20) DEFAULT 'active', -- active, completed, abandoned
    platform VARCHAR(20) NOT NULL, -- instagram, whatsapp, web
    
    -- Gift Context
    occasion VARCHAR(100) NOT NULL,
    occasion_date DATE,
    occasion_importance INTEGER CHECK (occasion_importance BETWEEN 1 AND 10),
    
    -- Budget & Constraints
    budget_min INTEGER, -- cents
    budget_max INTEGER, -- cents
    budget_flexibility VARCHAR(20), -- strict, flexible, no_limit
    
    -- Timing
    urgency_level INTEGER CHECK (urgency_level BETWEEN 1 AND 10),
    needed_by_date DATE,
    
    -- Intent & Emotion
    primary_emotion VARCHAR(50), -- love, gratitude, apology, celebration
    desired_reaction VARCHAR(100), -- surprise, joy, comfort, laughter
    relationship_goal VARCHAR(100), -- strengthen, maintain, repair, celebrate
    
    -- Session Outcome
    completed_at TIMESTAMP,
    chosen_gift_id UUID, -- Reference to final choice
    satisfaction_rating INTEGER CHECK (satisfaction_rating BETWEEN 1 AND 5),
    
    -- Rich Context (JSON for flexibility)
    conversation_context JSONB, -- Full conversation state
    extracted_insights JSONB, -- AI-derived insights
    decision_factors JSONB, -- What influenced the choice
    
    -- Metadata
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- === GIFT RECOMMENDATIONS ===
CREATE TABLE gift_recommendations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES gift_sessions(id) ON DELETE CASCADE,
    
    -- Recommendation Details
    product_id VARCHAR(255) NOT NULL, -- External product identifier
    product_data JSONB NOT NULL, -- Full product information
    recommendation_rank INTEGER NOT NULL,
    
    -- AI Reasoning
    confidence_score DECIMAL(5,4) NOT NULL, -- 0.0000 to 1.0000
    explanation TEXT NOT NULL,
    reasoning_factors JSONB, -- Detailed AI reasoning
    
    -- User Interaction
    user_reaction VARCHAR(20), -- viewed, liked, disliked, saved, purchased
    time_spent_viewing INTEGER DEFAULT 0, -- seconds
    user_feedback TEXT,
    
    -- Outcome Tracking
    was_purchased BOOLEAN DEFAULT FALSE,
    purchase_price INTEGER, -- cents
    purchase_date TIMESTAMP,
    
    -- Metadata
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- === GIFT OUTCOMES (Post-gift feedback) ===
CREATE TABLE gift_outcomes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id UUID NOT NULL REFERENCES gift_sessions(id),
    recommendation_id UUID REFERENCES gift_recommendations(id),
    user_id UUID NOT NULL REFERENCES users(id),
    recipient_id UUID NOT NULL REFERENCES recipients(id),
    
    -- Actual Outcome
    was_given BOOLEAN NOT NULL DEFAULT FALSE,
    given_date DATE,
    recipient_reaction VARCHAR(50), -- thrilled, happy, neutral, disappointed
    reaction_intensity INTEGER CHECK (reaction_intensity BETWEEN 1 AND 10),
    
    -- Relationship Impact
    relationship_impact DECIMAL(5,4), -- -1.0000 to 1.0000 change
    would_give_again BOOLEAN,
    would_recommend_to_others BOOLEAN,
    
    -- Learning Data
    what_worked TEXT,
    what_didnt_work TEXT,
    lessons_learned TEXT,
    surprise_factors TEXT, -- Unexpected outcomes
    
    -- Rich Outcome Data
    outcome_details JSONB, -- Photos, videos, detailed feedback
    follow_up_conversations JSONB, -- Related discussions
    
    -- Metadata
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- === OCCASIONS CALENDAR ===
CREATE TABLE occasions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    recipient_id UUID REFERENCES recipients(id) ON DELETE CASCADE,
    
    -- Occasion Details
    name VARCHAR(100) NOT NULL,
    occasion_type VARCHAR(50) NOT NULL, -- birthday, anniversary, holiday, milestone
    date DATE NOT NULL,
    is_recurring BOOLEAN DEFAULT FALSE,
    recurrence_pattern VARCHAR(50), -- yearly, monthly, custom
    
    -- Importance & Context
    importance_level INTEGER CHECK (importance_level BETWEEN 1 AND 10),
    cultural_significance VARCHAR(100),
    personal_significance TEXT,
    
    -- Gift Planning
    typical_budget_range INTEGER[], -- [min, max] in cents
    advance_planning_days INTEGER DEFAULT 14,
    reminder_schedule INTEGER[], -- Days before to remind
    
    -- Historical Data
    gifts_given_count INTEGER DEFAULT 0,
    last_gift_success_rating DECIMAL(5,4),
    
    -- Metadata
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- === USER PREFERENCES (Learned over time) ===
CREATE TABLE user_preferences (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    
    -- Gift Giving Style
    gifting_personality VARCHAR(50), -- thoughtful_planner, spontaneous, practical, sentimental
    effort_preference VARCHAR(50), -- high_effort, balanced, convenience_focused
    personalization_level VARCHAR(50), -- highly_personal, moderately_personal, functional
    
    -- Value System
    sustainability_importance INTEGER CHECK (sustainability_importance BETWEEN 1 AND 10),
    local_business_preference INTEGER CHECK (local_business_preference BETWEEN 1 AND 10),
    handmade_preference INTEGER CHECK (handmade_preference BETWEEN 1 AND 10),
    brand_consciousness INTEGER CHECK (brand_consciousness BETWEEN 1 AND 10),
    
    -- Budget Patterns
    budget_philosophy VARCHAR(50), -- value_focused, generous, budget_conscious
    splurge_occasions TEXT[], -- Which occasions justify higher spending
    
    -- Communication Style
    communication_formality VARCHAR(20), -- formal, casual, intimate
    humor_usage VARCHAR(20), -- frequent, occasional, rare
    emotional_expressiveness VARCHAR(20), -- very_expressive, moderate, reserved
    
    -- Learning Metadata
    confidence_level DECIMAL(5,4) NOT NULL DEFAULT 0.0000,
    last_updated TIMESTAMP NOT NULL DEFAULT NOW(),
    data_points_count INTEGER DEFAULT 0,
    
    -- Rich Preference Data
    detailed_preferences JSONB, -- Flexible preference storage
    learning_history JSONB, -- How preferences evolved
    
    UNIQUE(user_id)
);

-- === PERFORMANCE INDEXES ===
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_last_active ON users(last_active_at DESC);
CREATE INDEX idx_recipients_user_id ON recipients(user_id);
CREATE INDEX idx_recipients_importance ON recipients(user_id, importance_level DESC);
CREATE INDEX idx_gift_sessions_user_status ON gift_sessions(user_id, session_status);
CREATE INDEX idx_gift_sessions_created ON gift_sessions(created_at DESC);
CREATE INDEX idx_recommendations_session_rank ON gift_recommendations(session_id, recommendation_rank);
CREATE INDEX idx_recommendations_user_reaction ON gift_recommendations(user_reaction);
CREATE INDEX idx_outcomes_user_recipient ON gift_outcomes(user_id, recipient_id);
CREATE INDEX idx_occasions_user_date ON occasions(user_id, date);
CREATE INDEX idx_occasions_upcoming ON occasions(date) WHERE date >= CURRENT_DATE;

-- === JSONB INDEXES (for efficient JSON querying) ===
CREATE INDEX idx_recipients_personality ON recipients USING GIN (personality_traits);
CREATE INDEX idx_recipients_preferences ON recipients USING GIN (preferences);
CREATE INDEX idx_sessions_context ON gift_sessions USING GIN (conversation_context);
CREATE INDEX idx_recommendations_factors ON gift_recommendations USING GIN (reasoning_factors);
```

## **3. Neo4j: Relationship Graph Schema**

```cypher
// === CORE ENTITIES ===

// User nodes
CREATE CONSTRAINT user_id_unique IF NOT EXISTS FOR (u:User) REQUIRE u.id IS UNIQUE;
CREATE (u:User {
    id: "user_123",
    name: "Sarah Chen",
    created_at: timestamp(),
    
    // Social Graph Metrics
    network_size: 45,           // Total recipients
    active_relationships: 12,   // Regularly gifted to
    influence_score: 0.7,       // How often others copy her gifts
    
    // Behavioral Patterns
    gifting_frequency: "high",   // high, medium, low
    spontaneity_score: 0.3,     // 0 = planned, 1 = spontaneous
    reciprocity_expectation: 0.6 // How much they expect gifts back
})

// Recipient nodes (people in the network)
CREATE (r:Recipient {
    id: "recip_456",
    name: "Mom",
    real_name: "Linda Chen",
    
    // Network Position
    centrality_score: 0.9,      // How central in the gift network
    gift_recipient_rank: 1,     // 1 = most gifted to person
    
    // Gift Reception Patterns
    gratitude_expression: "high", // How they show appreciation
    gift_reciprocation_rate: 0.8, // How often they gift back
    preference_clarity: 0.6       // How clear their preferences are
})

// Gift nodes as relationship entities
CREATE (g:Gift {
    id: "gift_789",
    name: "Hand-knitted scarf",
    category: "handmade_clothing",
    
    // Gift Characteristics
    effort_level: 9,            // 1-10 effort investment
    personalization_level: 10,  // 1-10 how personalized
    surprise_factor: 7,         // 1-10 unexpectedness
    
    // Outcome Metrics
    success_score: 0.95,        // Overall success rating
    virality_score: 0.3,        // How much it inspired others
    memorable_score: 0.9        // How memorable it was
})

// Occasion nodes (temporal context)
CREATE (o:Occasion {
    id: "occasion_101",
    name: "Birthday 2024",
    type: "birthday",
    date: "2024-03-15",
    importance_level: 10
})

// === RELATIONSHIP TYPES WITH RICH PROPERTIES ===

// User-Recipient relationship (the core gift-giving relationship)
CREATE (u)-[:KNOWS {
    // Relationship Classification
    relationship_type: "family",
    relationship_label: "mother",
    relationship_depth: 10,         // 1-10 closeness scale
    relationship_since: "1992-03-15",
    
    // Communication Patterns
    communication_frequency: "daily",
    communication_channels: ["phone", "text", "in_person"],
    last_interaction: timestamp(),
    
    // Gift Exchange Dynamics
    gift_giving_direction: "bidirectional", // unidirectional, bidirectional
    gifts_given_count: 47,
    gifts_received_count: 52,
    last_gift_given: timestamp(),
    last_gift_received: timestamp(),
    
    // Emotional Temperature
    emotional_warmth: 0.95,         // 0-1 scale
    conflict_level: 0.1,            // 0-1 scale
    support_level: 0.9,             // How much they support each other
    
    // Gift Success Patterns
    average_gift_success: 0.85,     // Historical success rate
    preferred_gift_types: ["handmade", "experiential", "sentimental"],
    gift_failures: ["expensive_jewelry", "tech_gadgets"],
    
    // Relationship Trajectory  
    relationship_trend: "stable",    // growing, stable, declining
    predicted_future_importance: 0.95
}]->(r)

// Gift-giving relationship (specific gift exchange)
CREATE (u)-[:GAVE {
    // Gift Context
    occasion_id: "occasion_101",
    date: timestamp(),
    
    // Effort & Investment
    planning_time_hours: 12,
    financial_investment: 0,        // $0 for handmade
    emotional_investment: 0.95,     // 0-1 scale
    
    // Surprise & Timing
    surprise_level: 8,              // 1-10 scale
    timing_appropriateness: 0.9,    // 0-1 scale
    
    // Recipient Reaction
    immediate_reaction: "tears_of_joy",
    reaction_intensity: 10,         // 1-10 scale
    gratitude_expression: "overwhelming",
    
    // Relationship Impact
    relationship_strengthening: 0.15, // Change in relationship score
    memorable_factor: 0.95,         // How memorable this gift was
    story_worthiness: 0.9,          // Likelihood to be retold
    
    // Learning Value
    confidence_boost: 0.2,          // Boost to gift-giving confidence
    pattern_reinforcement: ["handmade_wins", "sentimental_over_expensive"]
}]->(g)

// Gift targeting relationship
CREATE (g)-[:INTENDED_FOR {
    appropriateness_score: 0.95,
    cultural_sensitivity: 0.9,
    timing_relevance: 0.85,
    personal_relevance: 1.0
}]->(r)

// Occasion context relationship
CREATE (g)-[:GIVEN_FOR {
    occasion_appropriateness: 0.9,
    timing_offset_days: 0,          // Days before/after occasion
    was_surprise: true
}]->(o)

// Gift similarity relationships (for pattern learning)
CREATE (g)-[:SIMILAR_TO {
    similarity_score: 0.85,
    shared_attributes: ["handmade", "practical", "sentimental"],
    shared_success_factors: ["personal_touch", "utility", "emotional_resonance"]
}]->(g2:Gift)

// User influence relationships (gift idea spreading)
CREATE (u)-[:INFLUENCED_BY {
    influence_type: "gift_inspiration",
    influence_strength: 0.7,
    specific_gift_id: "gift_789",
    adoption_delay_days: 14
}]->(u2:User)

// Recipient similarity (for cross-user recommendations)
CREATE (r)-[:SIMILAR_TO {
    similarity_score: 0.6,
    shared_traits: ["practical", "family_oriented", "handmade_appreciator"],
    successful_crossover_gifts: ["gift_789", "gift_456"]
}]->(r2:Recipient)

// === ADVANCED RELATIONSHIP PATTERNS ===

// Gift success clusters (gifts that work well together)
CREATE (g)-[:COMPLEMENTS {
    complementary_strength: 0.8,
    sequence_order: 1,              // First in a gift sequence
    occasion_synergy: 0.9
}]->(g2:Gift)

// Seasonal/temporal patterns
CREATE (g)-[:SEASONAL_PATTERN {
    season: "winter",
    month_preference: [11, 12, 1, 2],
    weather_dependency: 0.9,
    cultural_timing: "pre_holiday"
}]->(o)

// Cultural appropriateness mapping
CREATE (g)-[:APPROPRIATE_FOR {
    culture: "chinese_american",
    appropriateness_score: 0.9,
    cultural_significance: "high",
    taboo_level: 0.0
}]->(u)
```

## **4. Vector Embeddings Schema**

```python
class VectorEmbeddingModel:
    """Semantic representations for intelligent matching"""
    
    def embedding_specifications(self):
        return {
            "user_profile_embedding": {
                "dimensions": 1536,
                "model": "text-embedding-3-large",
                "update_frequency": "after_each_session",
                "components": [
                    # Demographic Context (0-100)
                    "age_cohort", "cultural_background", "location_context", "life_stage",
                    
                    # Personality Traits (100-200)
                    "openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism",
                    "risk_tolerance", "novelty_seeking", "aesthetic_preference",
                    
                    # Values & Beliefs (200-300)
                    "sustainability_importance", "local_support", "craftsmanship_appreciation",
                    "brand_consciousness", "price_sensitivity", "quality_focus",
                    
                    # Communication Style (300-400)
                    "formality_level", "humor_usage", "emotional_expressiveness", 
                    "directness", "relationship_maintenance_style",
                    
                    # Gift Giving Patterns (400-600)
                    "planning_vs_spontaneous", "effort_investment_typical", 
                    "personalization_importance", "surprise_preference",
                    "reciprocity_expectations", "occasion_prioritization",
                    
                    # Relationship Approach (600-800)
                    "family_closeness", "friendship_investment", "professional_boundaries",
                    "romantic_expression_style", "conflict_resolution_approach",
                    
                    # Learning Patterns (800-1000)
                    "feedback_responsiveness", "preference_consistency", 
                    "adaptation_speed", "cultural_sensitivity",
                    
                    # Contextual Preferences (1000-1536)
                    "seasonal_preferences", "budget_patterns", "timing_preferences",
                    "delivery_preferences", "presentation_importance"
                ],
                
                "metadata": {
                    "confidence_score": "float",
                    "last_updated": "timestamp",
                    "data_points_count": "integer",
                    "embedding_version": "string"
                }
            },
            
            "recipient_profile_embedding": {
                "dimensions": 1536,
                "model": "text-embedding-3-large", 
                "update_frequency": "after_gift_outcome",
                "components": [
                    # Demographic Profile (0-100)
                    "estimated_age", "inferred_culture", "lifestyle_indicators", "life_stage",
                    
                    # Personality Inference (100-300)
                    "extraversion_indicators", "openness_signals", "practical_vs_aesthetic",
                    "traditional_vs_modern", "individual_vs_social", "active_vs_contemplative",
                    
                    # Interests & Hobbies (300-600)  
                    "creative_pursuits", "physical_activities", "intellectual_interests",
                    "social_activities", "home_interests", "technology_adoption",
                    
                    # Values & Priorities (600-800)
                    "family_importance", "career_focus", "health_consciousness",
                    "environmental_concern", "community_involvement", "spiritual_inclination",
                    
                    # Gift Reception Patterns (800-1200)
                    "gratitude_expression_style", "surprise_appreciation", "practical_preference",
                    "sentimental_value_importance", "quality_vs_quantity", "experience_vs_material",
                    "handmade_appreciation", "luxury_comfort", "uniqueness_desire",
                    
                    # Relationship Context (1200-1400)
                    "with_gift_giver_history", "communication_patterns", "emotional_closeness",
                    "reciprocity_patterns", "boundary_preferences",
                    
                    # Contextual Factors (1400-1536)
                    "current_life_situation", "recent_major_events", "upcoming_occasions",
                    "housing_situation", "financial_apparent_status", "time_availability"
                ],
                
                "metadata": {
                    "relationship_to_user": "string",
                    "gift_success_history": "array",
                    "last_successful_gift": "string",
                    "confidence_score": "float"
                }
            },
            
            "gift_semantic_embedding": {
                "dimensions": 1536,
                "model": "text-embedding-3-large",
                "update_frequency": "daily_batch",
                "components": [
                    # Physical Characteristics (0-200)
                    "size_category", "weight_category", "material_composition", "durability",
                    "aesthetic_style", "color_palette", "texture_qualities", "visual_impact",
                    
                    # Functional Attributes (200-400)
                    "primary_purpose", "secondary_uses", "skill_required", "maintenance_needs",
                    "frequency_of_use", "learning_curve", "versatility", "accessibility",
                    
                    # Emotional Resonance (400-700)
                    "joy_potential", "comfort_factor", "excitement_level", "nostalgia_trigger",
                    "pride_inspiration", "surprise_factor", "humor_element", "romance_association",
                    "achievement_recognition", "care_expression", "thoughtfulness_signal",
                    
                    # Social & Cultural Dimensions (700-900)
                    "status_signaling", "conversation_starter", "social_acceptability",
                    "cultural_appropriateness", "generational_appeal", "gender_associations",
                    "religious_considerations", "political_implications",
                    
                    # Occasion Appropriateness (900-1100)
                    "birthday_suitability", "holiday_relevance", "anniversary_appropriateness",
                    "celebration_energy", "milestone_significance", "everyday_surprise_factor",
                    "apology_effectiveness", "congratulation_impact",
                    
                    # Practical Considerations (1100-1300)
                    "price_point_category", "value_perception", "shipping_complexity",
                    "storage_requirements", "presentation_needs", "customization_potential",
                    "return_possibility", "gift_wrap_suitability",
                    
                    # Recipient Matching Factors (1300-1536)
                    "age_appropriateness_range", "lifestyle_compatibility", "interest_alignment",
                    "personality_match", "relationship_depth_requirement", "cultural_sensitivity",
                    "effort_perception", "uniqueness_level", "memorability_factor"
                ],
                
                "metadata": {
                    "product_id": "string",
                    "price_usd": "float",
                    "availability_status": "string",
                    "vendor_id": "string",
                    "success_rate_overall": "float",
                    "cultural_tags": "array",
                    "occasion_tags": "array",
                    "last_updated": "timestamp"
                }
            },
            
            "relationship_context_embedding": {
                "dimensions": 768,
                "model": "text-embedding-3-small",  # Smaller for efficiency
                "update_frequency": "real_time",
                "components": [
                    # Relationship Dynamics (0-200)
                    "closeness_level", "communication_frequency", "emotional_temperature",
                    "support_patterns", "conflict_history", "shared_experiences_richness",
                    
                    # Gift Exchange History (200-400)
                    "historical_success_rate", "gift_value_patterns", "effort_reciprocity",
                    "surprise_patterns", "occasion_participation", "gratitude_patterns",
                    
                    # Current Context (400-600)
                    "recent_interactions", "relationship_trajectory", "life_event_impact",
                    "seasonal_patterns", "occasion_significance", "emotional_needs",
                    
                    # Future Considerations (600-768)
                    "relationship_goals", "anticipated_changes", "upcoming_occasions",
                    "investment_willingness", "risk_tolerance", "surprise_readiness"
                ]
            }
        }
```

## **5. Redis: Real-Time State Management**

```python
class RedisSchema:
    """Hot data for real-time personalization"""
    
    def cache_patterns(self):
        return {
            # User session state
            f"session:{user_id}:{session_id}": {
                "ttl": 3600,  # 1 hour
                "data": {
                    "conversation_context": {},
                    "current_recipient": {},
                    "extracted_preferences": {},
                    "recommendation_state": {},
                    "user_feedback_buffer": []
                }
            },
            
            # User profile hot cache
            f"user_profile:{user_id}": {
                "ttl": 86400,  # 24 hours
                "data": {
                    "preferences_vector": [],
                    "recent_recipients": [],
                    "active_occasions": [],
                    "recommendation_boost_factors": {}
                }
            },
            
            # Real-time recommendation cache
            f"recommendations:{session_id}": {
                "ttl": 1800,  # 30 minutes
                "data": {
                    "generated_recommendations": [],
                    "user_interactions": [],
                    "a_b_test_variant": "string",
                    "performance_metrics": {}
                }
            },
            
            # Gift success pattern cache
            f"gift_patterns:{user_id}": {
                "ttl": 604800,  # 1 week
                "data": {
                    "successful_gift_types": [],
                    "failed_gift_patterns": [],
                    "seasonal_preferences": {},
                    "recipient_specific_patterns": {}
                }
            }
        }
```

## **6. Event Sourcing: Behavioral Learning Schema**

```python
class EventSourcingModel:
    """Complete behavioral history for learning"""
    
    def event_types(self):
        return {
            "UserRegistered": {
                "user_id": "string",
                "registration_source": "string",
                "initial_preferences": "object",
                "timestamp": "datetime"
            },
            
            "ConversationStarted": {
                "user_id": "string",
                "session_id": "string",
                "platform": "string",
                "initial_intent": "string",
                "context": "object"
            },
            
            "RecipientMentioned": {
                "session_id": "string",
                "recipient_name": "string",
                "relationship_descriptor": "string",
                "emotional_context": "object",
                "new_information": "object"
            },
            
            "PreferenceRevealed": {
                "session_id": "string",
                "preference_type": "string",
                "preference_value": "any",
                "confidence": "float",
                "context": "string"
            },
            
            "GiftRecommended": {
                "session_id": "string",
                "recommendation_id": "string",
                "product_data": "object",
                "reasoning": "object",
                "confidence_score": "float",
                "personalization_factors": "array"
            },
            
            "UserReaction": {
                "session_id": "string",
                "recommendation_id": "string",
                "reaction_type": "string",  # viewed, liked, saved, purchased
                "reaction_intensity": "float",
                "time_spent": "integer",
                "feedback_text": "string"
            },
            
            "GiftPurchased": {
                "session_id": "string",
                "recommendation_id": "string",
                "actual_product": "object",
                "purchase_price": "float",
                "purchase_date": "datetime",
                "modifications_made": "array"
            },
            
            "GiftOutcomeReported": {
                "session_id": "string",
                "outcome_type": "string",  # success, neutral, failure
                "recipient_reaction": "object",
                "relationship_impact": "float",
                "lessons_learned": "array",
                "would_repeat": "boolean"
            },
            
            "RelationshipInsightGained": {
                "user_id": "string",
                "recipient_id": "string",
                "insight_type": "string",
                "insight_data": "object",
                "confidence": "float",
                "supporting_evidence": "array"
            },
            
            "SeasonalPatternDetected": {
                "user_id": "string",
                "pattern_type": "string",
                "pattern_data": "object",
                "recurrence": "string",
                "confidence": "float"
            }
        }
```

## **7. Data Flow & Integration Patterns**

```python
class DataIntegrationFlow:
    """How data flows between systems for maximum intelligence"""
    
    def integration_patterns(self):
        return {
            "real_time_flow": {
                "trigger": "User message received",
                "flow": [
                    "1. Extract info → PostgreSQL (recipients, sessions)",
                    "2. Update vectors → Vector DB (embeddings)",
                    "3. Query relationships → Neo4j (gift patterns)",
                    "4. Cache state → Redis (conversation context)",
                    "5. Log event → Event Store (behavioral learning)"
                ],
                "latency_target": "<200ms"
            },
            
            "batch_intelligence_update": {
                "frequency": "Hourly",
                "flow": [
                    "1. Aggregate events → Event Store analysis",
                    "2. Update user profiles → PostgreSQL + Vectors",
                    "3. Refresh relationship scores → Neo4j",
                    "4. Generate insights → All databases",
                    "5. Update ML models → Vector embeddings"
                ],
                "purpose": "Continuous learning and personalization improvement"
            },
            
            "gift_outcome_processing": {
                "trigger": "Gift outcome reported",
                "flow": [
                    "1. Record outcome → PostgreSQL",
                    "2. Update success patterns → Neo4j relationships",
                    "3. Adjust embeddings → Vector DB",
                    "4. Learn from outcome → Event Store",
                    "5. Improve future recommendations → All systems"
                ],
                "impact": "Improves recommendations for all similar users"
            }
        }
```

## **8. Key Design Principles**

### **Relationship-First Architecture**
- Every data point serves to understand human relationships better
- Gift transactions are secondary to relationship intelligence
- Data model optimizes for emotional understanding, not just product matching

### **Temporal Intelligence** 
- Complete history preservation through event sourcing
- Relationship evolution tracking over years
- Seasonal and lifecycle pattern recognition

### **Network Effect Maximization**
- Each user's data improves recommendations for similar users
- Relationship graphs create cross-user intelligence
- Cultural and demographic patterns benefit entire user base

### **Privacy by Design**
- Field-level encryption for sensitive relationship data
- Anonymized learning patterns that don't expose individual relationships
- User control over data sharing and deletion

### **Scalable Intelligence**
- Hybrid database approach allows independent scaling
- Vector embeddings enable semantic understanding at scale
- Graph relationships provide O(1) relationship traversal

This data model transforms Present Agent from a simple recommendation engine into a **Relationship Intelligence Platform** that understands the emotional economy of human connections through gifts.

The key insight: **We're not storing gift data. We're mapping the emotional architecture of human relationships.**