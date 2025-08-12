# Present Agent: Complete Product Development Guide

## 📋 Table of Contents

### [1. Project Overview](#1-project-overview)
- [Core Value Proposition](#core-value-proposition)
- [Success Metrics](#success-metrics)
- [Target Economics](#target-economics)

### [2. Business Model Canvas](#2-business-model-canvas)
- [Value Propositions](#value-propositions)
- [Customer Segments](#customer-segments)
- [Revenue Streams](#revenue-streams)
- [Key Resources](#key-resources)
- [Key Partnerships](#key-partnerships)
- [Customer Relationships](#customer-relationships)
- [Channels](#channels)
- [Key Activities](#key-activities)
- [Cost Structure](#cost-structure)

### [3. MVP Assumption Validation Framework](#3-mvp-assumption-validation-framework)
- [Core Assumptions to Test](#core-assumptions-to-test)
- [Pass/Fail Experiments](#passfail-experiments)
- [MVP Feature Scope](#mvp-feature-scope)
- [Validation Experiments](#validation-experiments)

### [4. Implementation Roadmap](#4-implementation-roadmap)
- [Implementation Steps](#implementation-steps)
- [Phase-by-Phase Breakdown](#phase-by-phase-breakdown)
- [Success Criteria & Kill Criteria](#success-criteria--kill-criteria)

### [5. Data Architecture](#5-data-architecture)
- [Multi-Database Hybrid System](#multi-database-hybrid-system)
- [PostgreSQL Schema](#postgresql-schema)
- [Neo4j Relationship Graph](#neo4j-relationship-graph)
- [Vector Embeddings](#vector-embeddings)

### [6. Simplified MVP Approach](#6-simplified-mvp-approach)
- [Minimal Viable Product](#minimal-viable-product)
- [Progressive Testing](#progressive-testing)
- [Cost Model](#cost-model)

### [7. Technical Specification](#7-technical-specification)
- [System Architecture](#system-architecture)
- [User Experience](#user-experience)
- [Technical Implementation](#technical-implementation)

---

# 1. Project Overview

## Core Value Proposition

Present Agent transforms gift-giving from stressful obligation to joyful relationship investment through AI-powered relationship intelligence. The platform understands the emotional architecture of human connections and provides hyper-personalized gift recommendations in under 2 minutes.

- **For Individuals**: AI that understands your relationships and finds perfect gifts in 2 minutes
- **For Recipients**: Receive gifts that genuinely express care and strengthen bonds  
- **For Society**: Reduce $75B annual gift waste through meaningful, targeted giving

## Success Metrics

### Market Validation
- **Product-Market Fit**: NPS >50, >70% find recommendations better than alternatives
- **Viral Coefficient**: >0.5 (each user brings 0.5 new users through gifts)
- **Network Effects**: Recommendation accuracy improves measurably with user base

### Business Viability
- **Unit Economics**: CAC/LTV <0.3, 18-month payback
- **Revenue Growth**: Path to $10K MRR, then $1M ARR scale
- **Market Penetration**: 100K users by year 2, 1M by year 5

## Target Economics
- **ARPU**: $50 with 40% gross margin
- **Payback**: 18-month customer acquisition cost recovery
- **Scale**: Path to $10K MRR, then $1M ARR potential

---

# 2. Business Model Canvas

## Value Propositions

### 🎯 Core Value
Transform gift-giving from stressful obligation to joyful relationship investment

- **For Individuals**: AI that understands your relationships and finds the best gifts in 2 minutes or less
- **For Recipients**: Receive gifts that genuinely express care and strengthen bonds
- **For Society**: Reduce $75B annual gift waste through meaningful, targeted giving and re-gifting

### Unique Value Drivers
- **Relationship intelligence** > product recommendations
- **Proprietary context and data** to help profile and refine individuals and what constitutes the best gifts for them
- **Complete experience orchestration** (conversation → unboxing → impact)
- **Plan, anticipate and never miss deadlines** for occasions

## Customer Segments

### Primary: Relationship-conscious gift givers, ages 25-55
- Urban/suburban professionals with disposable income
- Active on social platforms (Instagram/WhatsApp)
- Value relationships but time-constrained, mentally overloaded
- Give 5+ gifts annually to family, friends and colleagues, $30-200 per gift
- Care about being personal and thoughtful, creating a memorable moment and present for people they care about - easily

### Possible Secondary Segments
- Busy parents managing family gift obligations
- Long-distance relationship maintainers
- Corporate gift coordinators who want to stand out

## Revenue Streams

### Multi-layer Monetization
1. **Transaction-based** 
   - 5-10% commission on gift purchases
   - Premium delivery fees ($15-50)
   - Rush processing ($25+ for same-day)

**Target Economics**: $50 ARPU, 40% gross margin, 18-month payback

## Key Resources

### Data Assets (Primary Moat)
- Relationship intelligence database
- Gift outcome history (success/failure patterns)
- Cultural appropriateness knowledge base
- User behavioral patterns and preferences

### Technical Infrastructure
- 5-database hybrid architecture (PostgreSQL, Neo4j, Vector DB, Redis, Event Store)
- AI/ML pipeline (GPT-4.1, RAG, Vector search)
- Multi-platform integrations (Meta, WhatsApp, payment processors)

### Human Capital
- AI/ML engineers with personalization expertise
- Cultural consultants and relationship psychologists
- Partnership managers for vendor relationships

## Key Partnerships

### Technology Partners
- OpenAI (GPT-4.1 API access and optimization)
- Meta Business Platform (Instagram/Messenger integration)
- Vector database providers (Pinecone/Weaviate)
- Payment processors (Stripe, international)

### Commerce Partners
- Artisan marketplaces (Etsy, local craftspeople)
- Sustainable brands (BCorp, eco-friendly products)
- Experience providers (local activities, subscriptions)

### Strategic Alliances
- Wedding/event planning services
- Corporate wellness programs

## Customer Relationships

### Relationship Type: Personal AI Assistant (high intimacy, high frequency)

### Acquisition Strategy
- Organic viral growth through gift recipient experience
- Social proof through gift success stories
- Instagram/TikTok content marketing
- Influencer partnerships with lifestyle content creators

### Retention Mechanisms
- Relationship memory system (switching cost)
- Occasion calendar with proactive reminders
- Continuous learning improvement (gets better over time)
- Social features (gift inspiration sharing)

## Channels

### Primary Distribution
- Native messaging platform integrations (Instagram DM, WhatsApp)
- Progressive web app for complex interactions
- API integrations for third-party services

### Marketing Channels
- Social media advertising (Instagram, TikTok)
- Content marketing (relationship tips, gift guides)
- Referral program (both giver and recipient incentives)
- Partnership integrations (calendar apps, social platforms)

## Key Activities

### Product Development
- AI model training and optimization
- Cultural intelligence database expansion
- User experience refinement
- Platform integration development

### Operations
- Vendor relationship management
- Quality assurance and cultural sensitivity review
- Customer support and relationship coaching
- Data analysis and pattern recognition

### Marketing & Growth
- Content creation and social media presence
- Partnership development and management
- User onboarding and retention optimization
- Brand building and thought leadership

## Cost Structure

### Technology Costs (40% of expenses)
- AI/ML infrastructure and API costs (OpenAI, vector search)
- Database hosting and scaling (Neo4j, PostgreSQL, Redis)
- Development and engineering salaries

### Operations Costs (35% of expenses)
- Payment processing fees
- Customer acquisition costs
- Vendor relationship management
- Quality assurance and content moderation

### Overhead (25% of expenses)
- General administrative expenses
- Legal and compliance
- Office and remote work infrastructure
- Insurance and business services

---

# 3. MVP Assumption Validation Framework

## Core Assumptions to Test

### Assumption 1: Hybrid Intelligence Beats Pure Search
**Hypothesis**: A hybrid recommendation engine (product catalog + relationship data) produces better gift ideas than traditional search or browsing.

**Pass/Fail Experiment**:
- **Test**: A/B test hybrid recommendations vs Amazon/Google Shopping results
- **Metric**: Blind preference test - users pick which gifts they'd actually buy
- **Pass**: >70% prefer hybrid recommendations
- **Fail**: <50% preference or no statistical significance
- **Sample Size**: 100 comparison tests minimum

### Assumption 2: Memory Creates Compounding Value
**Hypothesis**: Users will share personal data if the system demonstrably improves with each interaction.

**Pass/Fail Experiment**:
- **Test**: Track recommendation relevance scores across 5+ interactions per user
- **Metric**: Measurable improvement in satisfaction from session 1 to session 5
- **Pass**: >30% improvement in relevance scores with memory
- **Fail**: <10% improvement or users stop sharing after session 2
- **Sample Size**: 50 users with 5+ sessions each

### Assumption 3: Conversational UI Unlocks Sharing
**Hypothesis**: People prefer conversational interaction and will share more personal context via chat than forms.

**Pass/Fail Experiment**:
- **Test**: Measure depth of information shared (relationship details, personal stories, emotions)
- **Metric**: Average data points collected per user via chat vs traditional quiz
- **Pass**: >3x more contextual data shared via conversation
- **Fail**: <1.5x more data or >40% drop-off rate
- **Sample Size**: 200 initial conversations

### Assumption 4: Speed + Learning = Retention
**Hypothesis**: Users get relevant suggestions in <2 minutes and system noticeably improves with feedback.

**Pass/Fail Experiment**:
- **Test**: Time to satisfaction + return rate after feedback incorporation
- **Metric**: Time to "I love this!" moment + 7-day return rate
- **Pass**: <2 min to satisfaction AND >40% return rate
- **Fail**: >3 minutes OR <20% return rate
- **Sample Size**: 100 users tracked for sufficient data

## MVP Feature Scope

### MUST HAVE (Phase 1)
```python
features = {
    "conversation_engine": {
        "natural_language_input": True,
        "relationship_extraction": True,
        "context_understanding": True,
        "emotion_detection": True
    },
    "hybrid_recommendation": {
        "product_catalog_search": True,  # 10K products minimum
        "relationship_matching": True,    # Context → product mapping
        "explanation_generation": True    # WHY this gift matches
    },
    "memory_system": {
        "user_identification": True,       # Anonymous but persistent
        "recipient_profiles": True,       # Remember people discussed
        "preference_learning": True       # Track what worked/didn't
    },
    "feedback_loop": {
        "quick_reactions": True,          # 👍/👎 on suggestions
        "outcome_tracking": True          # Did you buy? How did it go?
    }
}
```

### NICE TO HAVE (Phase 2)
- Voice input (test if easier than typing)
- Multiple platforms (start with one)
- Purchase integration (just track intent for now)
- Reminder system (not core to assumptions)

### NOT NEEDED FOR MVP
- Payment processing
- Shipping integration  
- Multi-language support
- B2B features
- Social sharing
- AR experiences

## Validation Experiments

### Experiment 1: Baseline Quality Test (Phase 1)
**Setup**: 
```python
def quality_test():
    # 20 test scenarios with persona + recipient + occasion
    scenarios = load_test_scenarios()
    
    for scenario in scenarios:
        # Generate recommendations three ways
        amazon_results = search_amazon(scenario)
        google_results = search_google_shopping(scenario)
        hybrid_results = present_agent_recommend(scenario)
        
        # Blind test with real users
        preference = user_blind_test(amazon, google, hybrid)
        
    return preference_distribution
```

**Success Criteria**: Hybrid wins >70% of blind tests

### Experiment 2: Memory Value Test (Phase 2)
**Setup**:
```python
def memory_value_test():
    users = recruit_test_users(n=50)
    
    for user in users:
        # Session 1: Cold start
        session_1_score = get_recommendation_score(user, memory=False)
        
        # Sessions 2-5: With accumulated memory
        for session in range(2, 6):
            score = get_recommendation_score(user, memory=True)
            improvement = (score - session_1_score) / session_1_score
            
    return average_improvement
```

**Success Criteria**: >30% improvement by session 5

### Experiment 3: Conversation Depth Test (Phase 1)
**Setup**:
```python
def conversation_depth_test():
    # Group A: Conversational UI
    chat_group = users[:100]
    chat_data_points = []
    
    for user in chat_group:
        conversation = conduct_chat_session(user)
        data_points = extract_relationship_details(conversation)
        chat_data_points.append(len(data_points))
    
    # Group B: Traditional form/quiz
    form_group = users[100:200]
    form_data_points = []
    
    for user in form_group:
        form_data = collect_via_form(user)
        form_data_points.append(len(form_data))
    
    return mean(chat_data_points) / mean(form_data_points)
```

**Success Criteria**: Chat collects >3x more useful data points

### Experiment 4: Speed & Return Test (Phase 2)
**Setup**:
```python
def speed_and_retention_test():
    users = recruit_test_users(n=100)
    
    metrics = {
        "time_to_satisfaction": [],
        "returned_within_7_days": []
    }
    
    for user in users:
        start_time = time.now()
        satisfaction = False
        
        while not satisfaction and time_elapsed < 10_minutes:
            recommendation = generate_recommendation(user)
            feedback = get_user_feedback(recommendation)
            if feedback.satisfied:
                satisfaction = True
                metrics["time_to_satisfaction"].append(time_elapsed)
        
        # Track if they return
        if user_returns_within_7_days(user):
            metrics["returned_within_7_days"].append(True)
    
    return metrics
```

**Success Criteria**: <2 min average AND >40% return rate

---

# 4. Implementation Roadmap

## Implementation Steps

### Phase 1: Foundation Infrastructure (Days 1-3)

#### Step 1: Project Setup
```bash
# Terminal commands to run
mkdir present_agent_mvp && cd present_agent_mvp
python -m venv venv && source venv/bin/activate
pip install fastapi uvicorn openai psycopg2-binary sqlalchemy python-dotenv pytest httpx

# Create project structure
touch .env requirements.txt README.md
mkdir -p app/{api,core,db,services,experiments}
```

**Deliverables**:
```python
# app/main.py - Basic FastAPI app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Present Agent MVP")
app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "0.1.0"}

# app/config.py - Configuration
from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    database_url: str = "postgresql://localhost/present_agent"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

#### Step 2: Database Models
```python
# app/db/models.py - Core data models
from sqlalchemy import Column, String, JSON, DateTime, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    conversation_count = Column(Integer, default=0)
    
class Session(Base):
    __tablename__ = "sessions"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    context = Column(JSON)  # Extracted relationship data
    recommendations = Column(JSON)  # Generated recommendations
    feedback = Column(JSON)  # User feedback
    created_at = Column(DateTime, default=datetime.utcnow)
    time_to_satisfaction = Column(Float)  # Seconds

class Recipient(Base):
    __tablename__ = "recipients"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    name = Column(String)
    relationship = Column(String)
    attributes = Column(JSON)  # Interests, age, etc.
    gift_history = Column(JSON)  # Past successful/failed gifts
```

### Phase 2: Conversation Engine (Days 4-6)

#### Step 3: Basic Chat Flow
```python
# app/services/conversation.py
from openai import OpenAI
from typing import Dict, Optional

class ConversationEngine:
    def __init__(self):
        self.client = OpenAI()
        self.extraction_prompt = """
        Extract from user message:
        - recipient: who they're shopping for
        - relationship: how they're related
        - occasion: what the gift is for
        - budget: price range
        - interests: recipient's interests
        - context: emotional context or special requirements
        
        Return as JSON.
        """
    
    def process_message(self, message: str, history: list = None) -> Dict:
        # Extract context from message
        context = self.extract_context(message, history)
        
        # Identify missing information
        missing = self.get_missing_info(context)
        
        if missing:
            return {
                "type": "clarification",
                "question": self.generate_clarifying_question(missing[0]),
                "context": context
            }
        
        return {
            "type": "ready_for_recommendations",
            "context": context
        }
    
    def extract_context(self, message: str, history: list = None) -> Dict:
        messages = [
            {"role": "system", "content": self.extraction_prompt},
            {"role": "user", "content": message}
        ]
        
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)
```

#### Step 4: Natural Question Generation
```python
# app/services/conversation.py (continued)
def generate_clarifying_question(self, missing_field: str) -> str:
    questions = {
        "recipient": "Who are you shopping for?",
        "relationship": "How do you know them? (friend, family, colleague?)",
        "occasion": "What's the occasion? (birthday, holiday, just because?)",
        "budget": "What's your budget range?",
        "interests": "What are they interested in? Any hobbies?",
    }
    
    # Make it conversational
    base_question = questions.get(missing_field, f"Tell me more about {missing_field}")
    
    # Add context-aware follow-up
    enhancer_prompt = f"""
    Make this question feel natural and conversational: "{base_question}"
    Keep it under 20 words. Be warm and helpful.
    """
    
    response = self.client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": enhancer_prompt}],
        max_tokens=50
    )
    
    return response.choices[0].message.content
```

#### Step 5: Context Validation
```python
# app/services/validator.py
class ContextValidator:
    def validate_context(self, context: Dict) -> tuple[bool, list]:
        required_fields = ['recipient', 'relationship', 'occasion']
        missing = []
        
        for field in required_fields:
            if not context.get(field):
                missing.append(field)
        
        # Validate budget if provided
        if context.get('budget'):
            if not self.parse_budget(context['budget']):
                missing.append('budget_clarification')
        
        return len(missing) == 0, missing
```

### Phase 3: Product Catalog & Hybrid Recommendation (Days 7-9)

#### Step 6: Product Catalog Setup
```python
# app/services/catalog.py
import pandas as pd
from typing import List, Dict

class ProductCatalog:
    def __init__(self):
        self.products = self.load_products()
        self.embeddings = self.load_embeddings()
    
    def load_products(self) -> pd.DataFrame:
        # Load 10K curated products
        # For MVP: Use scraped data from Amazon, Etsy, local stores
        products = pd.read_csv('data/products.csv')
        return products
    
    def search(self, query: str, filters: Dict = None) -> List[Dict]:
        # Basic text search
        results = self.products[
            self.products['description'].str.contains(query, case=False)
        ]
        
        # Apply filters
        if filters:
            if 'min_price' in filters:
                results = results[results['price'] >= filters['min_price']]
            if 'max_price' in filters:
                results = results[results['price'] <= filters['max_price']]
            if 'category' in filters:
                results = results[results['category'] == filters['category']]
        
        return results.head(50).to_dict('records')
```

#### Step 7: Hybrid Recommender
```python
# app/services/recommender.py
from typing import List, Dict
import openai

class HybridRecommender:
    def __init__(self):
        self.catalog = ProductCatalog()
        self.client = OpenAI()
    
    def recommend(self, context: Dict, user_memory: Dict = None) -> List[Dict]:
        # Step 1: Create search query from context
        search_query = self.context_to_query(context)
        
        # Step 2: Get catalog matches
        catalog_results = self.catalog.search(
            query=search_query,
            filters={
                'min_price': context.get('budget_min', 0),
                'max_price': context.get('budget_max', 1000)
            }
        )
        
        # Step 3: Rank by relationship fit
        ranked = self.rank_by_relationship(catalog_results, context)
        
        # Step 4: Apply memory if available
        if user_memory:
            ranked = self.apply_user_preferences(ranked, user_memory)
        
        # Step 5: Generate explanations for top 3
        top_3 = ranked[:3]
        return self.add_explanations(top_3, context)
```

#### Step 8: Explanation Generation
```python
# app/services/recommender.py (continued)
def add_explanations(self, products: List[Dict], context: Dict) -> List[Dict]:
    recommendations = []
    
    for product in products:
        explanation_prompt = f"""
        Explain why this gift is perfect:
        Gift: {product['name']} - {product['description']}
        For: {context.get('relationship')}
        Occasion: {context.get('occasion')}
        Their interests: {context.get('interests')}
        
        Write a 2-sentence explanation that:
        1. Connects the gift to something specific they shared
        2. Explains the emotional impact
        
        Be warm and personal.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": explanation_prompt}],
            max_tokens=100
        )
        
        explanation = response.choices[0].message.content
        
        recommendations.append({
            "product": product,
            "explanation": explanation,
            "confidence": product.get('relationship_score', 0) / 10
        })
    
    return recommendations
```

### Phase 4: Memory System (Days 10-12)

#### Step 9: User Memory Storage
```python
# app/services/memory.py
from typing import Dict, List
import json

class MemorySystem:
    def __init__(self, db_session):
        self.db = db_session
    
    def remember_session(self, user_id: str, session_data: Dict):
        # Store conversation context
        session = Session(
            user_id=user_id,
            context=session_data['context'],
            recommendations=session_data['recommendations'],
            created_at=datetime.utcnow()
        )
        self.db.add(session)
        
        # Extract and store recipient info
        self.remember_recipient(user_id, session_data['context'])
        
        self.db.commit()
```

#### Step 10: Learning from Feedback
```python
# app/services/memory.py (continued)
def learn_from_feedback(self, session_id: str, feedback: Dict):
    session = self.db.query(Session).filter_by(id=session_id).first()
    
    if not session:
        return
    
    # Store feedback
    session.feedback = feedback
    
    # Update recipient preferences based on feedback
    if feedback.get('purchased'):
        self.boost_preference(session.user_id, session.recommendations[feedback['index']])
    elif feedback.get('disliked'):
        self.decrease_preference(session.user_id, session.recommendations[feedback['index']])
    
    # Calculate time to satisfaction
    if feedback.get('satisfied'):
        session.time_to_satisfaction = feedback.get('time_seconds')
    
    self.db.commit()
```

#### Step 11: Memory-Enhanced Recommendations
```python
# app/services/recommender.py (updated)
def apply_user_preferences(self, products: List[Dict], user_memory: Dict) -> List[Dict]:
    # Boost products similar to past successes
    preferences = user_memory.get('preferences', {})
    
    for product in products:
        boost_score = 0
        
        # Check against successful categories
        if product['category'] in preferences.get('successful_categories', []):
            boost_score += 0.2
        
        # Check against failed categories
        if product['category'] in preferences.get('failed_categories', []):
            boost_score -= 0.3
        
        # Check price range preferences
        if self.in_preferred_price_range(product['price'], preferences):
            boost_score += 0.1
        
        product['preference_score'] = product.get('relationship_score', 5) + boost_score
    
    return sorted(products, key=lambda x: x['preference_score'], reverse=True)
```

### Phase 5: Experiment Framework (Days 13-14)

#### Step 12: A/B Testing Setup
```python
# app/experiments/ab_test.py
import random
from typing import Dict, Any
from collections import defaultdict

class ExperimentFramework:
    def __init__(self):
        self.experiments = {
            'hybrid_vs_search': {
                'variants': ['control_search', 'treatment_hybrid'],
                'metrics': ['preference_rate', 'time_to_satisfaction']
            },
            'memory_value': {
                'variants': ['no_memory', 'with_memory'],
                'metrics': ['session_improvement', 'return_rate']
            }
        }
        self.assignments = {}  # User → variant mapping
        self.metrics = defaultdict(list)
    
    def assign_variant(self, user_id: str, experiment: str) -> str:
        # Consistent assignment for user
        key = f"{user_id}_{experiment}"
        
        if key not in self.assignments:
            variants = self.experiments[experiment]['variants']
            self.assignments[key] = random.choice(variants)
        
        return self.assignments[key]
```

#### Step 13: Assumption Validation Tests
```python
# app/experiments/validators.py
from scipy import stats

class AssumptionValidator:
    def __init__(self, experiment_framework):
        self.experiments = experiment_framework
    
    def validate_assumption_1_hybrid_quality(self) -> Dict:
        """Test: Hybrid beats pure search"""
        results = self.experiments.get_results('hybrid_vs_search')
        
        control_pref = results['control_search']['preference_rate']['values']
        treatment_pref = results['treatment_hybrid']['preference_rate']['values']
        
        # Statistical test
        t_stat, p_value = stats.ttest_ind(treatment_pref, control_pref)
        
        # Success criteria: >70% prefer hybrid
        treatment_mean = sum(treatment_pref) / len(treatment_pref) if treatment_pref else 0
        
        return {
            'pass': treatment_mean > 0.7 and p_value < 0.05,
            'preference_rate': treatment_mean,
            'p_value': p_value,
            'sample_size': len(treatment_pref)
        }
```

### Phase 6: API & Testing Interface (Days 15-16)

#### Step 14: REST API
```python
# app/api/chat.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None

class ChatResponse(BaseModel):
    user_id: str
    type: str  # 'clarification' or 'recommendations'
    content: Any
    context: Dict

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Get or create user
    user_id = request.user_id or str(uuid.uuid4())
    
    # Get user memory
    memory = memory_system.get_user_context(user_id)
    
    # Process message
    result = conversation_engine.process_message(
        request.message,
        memory.get('recent_sessions', [])
    )
    
    # If ready for recommendations
    if result['type'] == 'ready_for_recommendations':
        # Assign to experiment variant
        variant = experiments.assign_variant(user_id, 'hybrid_vs_search')
        
        if variant == 'treatment_hybrid':
            recommendations = hybrid_recommender.recommend(
                result['context'],
                memory
            )
        else:
            recommendations = basic_search.search(result['context'])
        
        # Store session
        memory_system.remember_session(user_id, {
            'context': result['context'],
            'recommendations': recommendations
        })
        
        return ChatResponse(
            user_id=user_id,
            type='recommendations',
            content=recommendations,
            context=result['context']
        )
    
    # Need clarification
    return ChatResponse(
        user_id=user_id,
        type='clarification',
        content=result['question'],
        context=result.get('context', {})
    )
```

#### Step 15: Launch & Monitoring
```python
# app/monitoring.py
from datetime import datetime, timedelta
import json

class MetricsDashboard:
    def __init__(self, db_session, experiments):
        self.db = db_session
        self.experiments = experiments
    
    def get_assumption_status(self) -> Dict:
        return {
            'assumption_1_hybrid_quality': self.check_hybrid_quality(),
            'assumption_2_memory_value': self.check_memory_value(),
            'assumption_3_conversation_depth': self.check_conversation_depth(),
            'assumption_4_speed_retention': self.check_speed_retention()
        }
```

## Success Criteria & Kill Criteria

### Phase 1 Checkpoint
- [ ] Assumption 1: Hybrid quality test complete with 100+ tests
- [ ] Assumption 3: Conversation depth measured with 200+ users
- [ ] **Decision**: Continue if 2/2 assumptions validated

### Phase 2 Final Decision  
- [ ] All 4 assumptions tested with statistical significance
- [ ] **GO if**: 3/4 assumptions clearly validated
- [ ] **PIVOT if**: 2/4 assumptions validated (adjust approach)
- [ ] **KILL if**: <2 assumptions validated

---

# 5. Data Architecture

## Multi-Database Hybrid System

### Core Philosophy: The Relationship-Centric Model
Present Agent's data model is designed around **relationships, not transactions**. Every piece of data serves to understand and enhance human connections through gifting.

### 1. Multi-Database Architecture

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

## PostgreSQL Schema

### Core Transactional Schema

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
```

## Neo4j Relationship Graph

### Relationship Graph Schema

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
```

## Vector Embeddings

### Semantic Representations for Intelligent Matching

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
                    
                    # Gift Giving Patterns (400-600)
                    "planning_vs_spontaneous", "effort_investment_typical", 
                    "personalization_importance", "surprise_preference",
                    "reciprocity_expectations", "occasion_prioritization",
                    
                    # Relationship Approach (600-800)
                    "family_closeness", "friendship_investment", "professional_boundaries",
                    "romantic_expression_style", "conflict_resolution_approach"
                ]
            },
            
            "gift_semantic_embedding": {
                "dimensions": 1536,
                "model": "text-embedding-3-large",
                "components": [
                    # Physical Characteristics (0-200)
                    "size_category", "weight_category", "material_composition", "durability",
                    "aesthetic_style", "color_palette", "texture_qualities", "visual_impact",
                    
                    # Emotional Resonance (400-700)
                    "joy_potential", "comfort_factor", "excitement_level", "nostalgia_trigger",
                    "pride_inspiration", "surprise_factor", "humor_element", "romance_association",
                    
                    # Social & Cultural Dimensions (700-900)
                    "status_signaling", "conversation_starter", "social_acceptability",
                    "cultural_appropriateness", "generational_appeal", "gender_associations",
                    
                    # Occasion Appropriateness (900-1100)
                    "birthday_suitability", "holiday_relevance", "anniversary_appropriateness",
                    "celebration_energy", "milestone_significance", "everyday_surprise_factor"
                ]
            }
        }
```

---

# 6. Simplified MVP Approach

## Minimal Viable Product

### Core Hypothesis
**People will trust an AI to help them find meaningful gifts if it asks the right questions about their relationships.**

### Riskiest Assumptions to Test First

#### Risk #1: Privacy vs Value Trade-off
**Assumption**: Users will share intimate relationship details with an AI
**Test**: Can we get users to describe their relationships naturally?
**Kill Criteria**: <20% share beyond basic demographics

#### Risk #2: AI Cost Viability  
**Assumption**: We can deliver value at <$2 per recommendation
**Test**: Measure actual GPT-4 costs per successful recommendation
**Kill Criteria**: >$5 per recommendation with no optimization path

#### Risk #3: Relationship Intelligence > Product Search
**Assumption**: Users prefer relationship-based recommendations over simple product search
**Test**: A/B test relationship questions vs product preferences
**Kill Criteria**: No measurable improvement in satisfaction

### The Absolute Minimum Product

#### What We Ship (Initial Release)
- **One Channel**: Instagram DM only
- **One Flow**: Text-based conversation
- **One Database**: PostgreSQL only (no complex architecture yet)
- **One AI**: GPT-4-turbo (cheaper than GPT-4.1)
- **No Authentication**: Anonymous sessions only
- **No Memory**: Each conversation starts fresh

#### Core Experience (30 lines of prompting)
```
User: "Hi"
Bot: "Hi! I help find meaningful gifts. Who are you shopping for?"
User: "My mom"
Bot: "Tell me 3 things about your relationship with your mom"
User: "[Shares details]"
Bot: "What's the occasion?"
User: "Her birthday"
Bot: "What's your budget?"
User: "$50-100"
Bot: "Based on what you shared... [3 recommendations with WHY they match]"
```

#### Technical Stack (Minimal)
```python
# Entire MVP in ~500 lines of code
- FastAPI (1 webhook endpoint)
- PostgreSQL (3 tables: sessions, messages, recommendations)  
- OpenAI API (GPT-4-turbo)
- Instagram Webhook API
- Heroku (free tier)
```

## Progressive Testing

### Phase 0: Manual Testing (No Code)
**Build**: Nothing - use your personal Instagram to manually chat with 10 friends
**Test**: Will people share relationship details via DM?
**Measure**: 
- How many share personal details?
- What questions unlock sharing?
- What makes them uncomfortable?
**Decision Point**: 
- ✅ Continue if >50% share meaningful details
- ❌ Kill if people refuse to engage

### Phase 1: Wizard of Oz (Minimal Code)
**Build**: 
- Instagram webhook receiver (50 lines)
- Human-powered responses with templates
- Simple PostgreSQL logging

**Test**: Can we deliver value manually?
**Measure**:
- Time to find good recommendations
- User satisfaction (1-5 rating)
- What patterns emerge?

**Decision Point**:
- ✅ Continue if satisfaction >3.5/5
- ❌ Pivot if we can't find good gifts manually

### Phase 2: Basic AI Integration
**Build**:
- GPT-4-turbo integration (100 lines)
- Relationship extraction prompt
- Basic recommendation generation

**Test**: Can AI extract relationship context and recommend?
**Measure**:
- Cost per conversation
- Recommendation relevance (user feedback)
- Response time

**Key Prompt to Test**:
```python
prompt = """
User wants gift for: {recipient}
Relationship details: {details}
Occasion: {occasion}
Budget: {budget}

Generate 3 gift recommendations that:
1. Connect to specific relationship details shared
2. Explain WHY this gift matches their relationship
3. Include emotional impact prediction

Format: JSON with gift, reason, where_to_buy
"""
```

**Decision Point**:
- ✅ Continue if cost <$2 and relevance >60%
- ❌ Pivot to simpler prompting or kill

## Cost Model

### Per Conversation Costs
- GPT-4-turbo: ~$0.30 (assuming 3K tokens in, 1K out)
- Instagram API: Free
- Heroku: Free tier
- PostgreSQL: Free tier

### Assumptions to Validate
- Conversations average 5-7 messages
- 30% return rate
- 20% show purchase intent
- 10% actually purchase (generating commission)

### Viability Threshold
**Break-even requirement**: 
- Need 10% purchase rate with $50 average order value
- $5 commission per purchase
- Cost per conversation: $0.30
- Need 1 purchase per 16 conversations to break even

---

# 7. Technical Specification

## System Architecture

### Present Agent: MVP Prototype Specification

#### Problem Statement
Gift-giving creates stress for millions. People struggle to find meaningful gifts, remember occasions, and shop within their values. We need to validate if an AI assistant can make gifting truly easy and thoughtful.

#### Solution Vision
A lightweight AI chatbot that starts simple - learning about one user and helping them find one great gift. Ship weekly, learn fast, iterate based on real user feedback.

### MVP Scope - Weekly Iterations

#### Phase 1: Basic Chat Interface ✅
**Ship:** Working chatbot that responds on ONE platform (Instagram DM)
**Features:**
- Basic greeting and introduction
- Collect user name and one gift need
- Hardcoded gift suggestions (no AI yet)
- Simple conversation flow

**Success Metric:** 10 users complete a full conversation

**Implementation:**
```
/prototype/
  ├── webhook.py         # Instagram webhook handler
  ├── chat_handler.py    # Basic message processing
  └── templates.py       # Response templates
```

#### Phase 2: AI-Powered Recommendations 🤖
**Ship:** GPT-4 integration for personalized suggestions
**Features:**
- Ask about recipient (who, occasion, interests)
- Generate 3 personalized gift ideas using AI
- Remember conversation context during session

**Success Metric:** 50% of users find suggestions helpful

**Implementation:**
```
  ├── ai_service.py      # OpenAI integration
  └── prompts.py         # Gift recommendation prompts
```

### Technical Approach - Keep It Simple

#### Minimal Stack
```
Backend:
- Python + FastAPI (simple, fast)
- PostgreSQL (user data)
- Redis (session cache)
- OpenAI API (recommendations)

Integrations:
- Meta Webhooks API (Instagram/Messenger)
- WhatsApp Business API

Deployment:
- Single Heroku dyno to start
- Upgrade as needed
```

#### Core Data Model (Start Simple)
```python
User:
  - id
  - instagram_id
  - name
  - values: ["eco", "local"]
  - created_at

Conversation:
  - id
  - user_id
  - messages: JSON
  - created_at

Gift:
  - id
  - user_id
  - recipient_name
  - occasion
  - suggestions: JSON
  - selected: String
  - created_at
```

## User Experience

### Primary user journey
1. Discovers via Instagram ad → DMs Present Agent
2. Brief onboarding (name, first gift need)
3. Describes recipient in natural language
4. Receives 3 curated suggestions with reasoning
5. Saves favorite for later or gets purchase link
6. Returns for next occasion with context retained

### Core interactions
- Natural language chat (no forms/menus)
- Visual product cards with descriptions
- One-tap save/share functionality
- Quick feedback thumbs up/down

### Edge cases
- Group gifts coordination
- International shipping needs
- Budget constraints mid-conversation
- Switching between platforms (Instagram → WhatsApp)

## Technical Implementation

### Architecture outline
```
Relationship Intelligence Platform (5-Database Hybrid)

User Interaction Layer:
Instagram/WhatsApp → FastAPI → Real-time Processing

Data Intelligence Layer:
├── PostgreSQL (Core transactions, users, sessions)
├── Neo4j (Relationship graph, social patterns)  
├── Vector DB (Semantic embeddings, cultural intelligence)
├── Redis (Real-time state, conversation context)
└── Event Store (Complete behavioral history, learning)

AI/ML Layer:
├── GPT-4.1 (Conversation & reasoning)
├── RAG System (Gift catalog + cultural knowledge)
├── Vector Search (Semantic gift matching)
└── Predictive Models (Relationship trajectory, timing)

Experience Layer:
├── AR Unboxing (Enhanced gift presentation)
├── AI Card Writer (Personalized messages)
├── Smart Packaging (Context-aware presentation)
└── Outcome Tracking (Relationship impact measurement)
```

### Complexity points
- **Highest:** Multi-modal relationship understanding across cultural contexts
- **High:** Real-time personalization with sub-200ms response times
- **Medium:** Cross-platform conversation continuity and state management
- **Medium:** Scaling AI costs while maintaining quality (GPT-4.1 optimization)

### Dependencies
- Meta Business Platform approval (Instagram/Messenger webhooks)
- OpenAI API (GPT-4.1 with 1M context window)
- Neo4j Aura (Managed graph database for relationships)
- Vector database service (Pinecone or Weaviate)
- Product catalog partnerships and real-time inventory
- Payment processing with international support
- AR development frameworks (React Native + AR.js)

---

*This comprehensive product guide contains all the strategic, business, and implementation details needed to build Present Agent. Use this as your primary reference throughout the development process.*