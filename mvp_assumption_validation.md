# Present Agent MVP: Assumption Validation Framework

## 🎯 Core Assumptions to Validate

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
- **Pass**: <2 min to satisfaction AND >40% return within 7 days
- **Fail**: >3 minutes OR <20% return rate
- **Sample Size**: 100 users tracked over 2 weeks

---

## 🏗 MVP Feature Scope (Only What Tests Assumptions)

### MUST HAVE (Week 1-2)
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

### NICE TO HAVE (Week 3-4)
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

---

## 📐 Technical Architecture (Minimal Viable)

```python
# Simplified from 5-database to 2-database architecture
architecture = {
    "databases": {
        "postgresql": "Users, sessions, recipients, feedback",
        "vector_db": "Semantic matching, memory embeddings"
        # NO Neo4j, Redis, or Event Store yet
    },
    "ai_stack": {
        "gpt-4-turbo": "Conversation and reasoning",
        "embeddings": "text-embedding-3-small",  # Cheaper
        "rag": "Basic product catalog retrieval"
    },
    "product_data": {
        "source": "Scraped/API from Amazon, Etsy, local stores",
        "size": "10,000 curated products",  # Not millions
        "update": "Weekly batch updates"    # Not real-time
    }
}
```

---

## 🧪 Validation Experiments

### Experiment 1: Baseline Quality Test (Week 1)
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

### Experiment 2: Memory Value Test (Week 2)
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

### Experiment 3: Conversation Depth Test (Week 1)
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

### Experiment 4: Speed & Return Test (Week 2-3)
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

## 💻 Coding Plan & Sequence

### Phase 1: Foundation (Days 1-3)
```bash
# Project setup
mkdir present_agent_mvp && cd present_agent_mvp
python -m venv venv && source venv/bin/activate

# Install core dependencies only
pip install fastapi openai psycopg2-binary python-dotenv pytest
```

**Files to create**:
```python
present_agent_mvp/
├── app.py                 # FastAPI main application
├── models.py              # SQLAlchemy models (User, Recipient, Session)
├── conversation.py        # Chat logic and context extraction
├── recommender.py         # Hybrid recommendation engine
├── memory.py              # User memory and learning system
└── experiments.py         # A/B testing framework
```

### Phase 2: Core Conversation Engine (Days 4-6)
```python
# conversation.py
class ConversationEngine:
    def __init__(self):
        self.client = OpenAI()
        
    def extract_relationship_context(self, message: str) -> dict:
        """Extract recipient, occasion, relationship details"""
        prompt = """
        Extract: who (relationship), occasion, budget, 
        interests, emotional context, urgency
        """
        return self.parse_gpt_response(prompt, message)
    
    def generate_clarifying_questions(self, context: dict) -> str:
        """Ask for missing critical information"""
        missing = self.identify_missing_context(context)
        return self.create_natural_question(missing[0])
```

### Phase 3: Hybrid Recommendation Engine (Days 7-9)
```python
# recommender.py
class HybridRecommender:
    def __init__(self):
        self.product_catalog = self.load_catalog()  # 10K products
        self.embeddings = self.load_embeddings()
        
    def recommend(self, context: dict, user_history: dict) -> list:
        # Step 1: Semantic search in product catalog
        product_matches = self.semantic_search(
            query=self.context_to_query(context),
            limit=50
        )
        
        # Step 2: Filter by relationship appropriateness
        filtered = self.apply_relationship_filters(
            products=product_matches,
            relationship=context['relationship'],
            occasion=context['occasion']
        )
        
        # Step 3: Personalize based on history
        personalized = self.apply_user_preferences(
            products=filtered,
            user_history=user_history
        )
        
        # Step 4: Generate explanations
        return self.add_explanations(personalized[:3], context)
```

### Phase 4: Memory System (Days 10-12)
```python
# memory.py
class MemorySystem:
    def __init__(self, db_connection):
        self.db = db_connection
        
    def remember_recipient(self, user_id: str, recipient_data: dict):
        """Store recipient profile for future use"""
        embedding = self.create_recipient_embedding(recipient_data)
        self.db.store_recipient(user_id, recipient_data, embedding)
    
    def learn_from_feedback(self, user_id: str, recommendation_id: str, 
                           feedback: str):
        """Update preferences based on feedback"""
        if feedback == 'purchased':
            self.boost_similar_products(recommendation_id)
        elif feedback == 'disliked':
            self.decrease_similar_products(recommendation_id)
    
    def get_user_context(self, user_id: str) -> dict:
        """Retrieve all learned context for better recommendations"""
        return {
            'recipients': self.db.get_recipients(user_id),
            'preferences': self.db.get_preferences(user_id),
            'successful_gifts': self.db.get_successes(user_id)
        }
```

### Phase 5: Experiment Framework (Days 13-14)
```python
# experiments.py
class ExperimentRunner:
    def __init__(self):
        self.variants = {}
        self.metrics = defaultdict(list)
    
    def run_ab_test(self, user_id: str, experiment: str):
        """Randomly assign variant and track metrics"""
        variant = self.assign_variant(user_id, experiment)
        
        if experiment == "hybrid_vs_traditional":
            if variant == "control":
                return self.traditional_search()
            else:
                return self.hybrid_recommendation()
    
    def track_metric(self, experiment: str, metric: str, value: float):
        """Store metrics for analysis"""
        self.metrics[f"{experiment}_{metric}"].append(value)
    
    def analyze_results(self, experiment: str):
        """Calculate statistical significance"""
        control = self.metrics[f"{experiment}_control"]
        treatment = self.metrics[f"{experiment}_treatment"]
        return ttest_ind(control, treatment)
```

### Phase 6: MVP Testing Interface (Days 15-16)
```python
# Simple web interface for testing
@app.post("/chat")
async def chat(message: str, user_id: str = None):
    # Create or retrieve user session
    if not user_id:
        user_id = str(uuid.uuid4())
    
    # Extract context from message
    context = conversation_engine.extract_context(message)
    
    # Get user memory
    user_history = memory.get_user_context(user_id)
    
    # Generate recommendations
    recommendations = recommender.recommend(context, user_history)
    
    # Track metrics
    experiments.track_metric("time_to_recommendation", time.elapsed)
    
    # Return response
    return {
        "user_id": user_id,
        "recommendations": recommendations,
        "explanation": generate_explanation(recommendations, context)
    }

@app.post("/feedback")
async def feedback(user_id: str, recommendation_id: str, rating: str):
    # Learn from feedback
    memory.learn_from_feedback(user_id, recommendation_id, rating)
    
    # Track for experiments
    experiments.track_metric("feedback_rate", 1 if rating else 0)
    
    return {"status": "learned"}
```

---

## 📊 Success Metrics Dashboard

```python
# Real-time metrics to track
metrics = {
    "assumption_1_hybrid_quality": {
        "current": "68%",  # % who prefer hybrid
        "target": "70%",
        "status": "❌ Below threshold"
    },
    "assumption_2_memory_value": {
        "current": "45%",  # Improvement session 1 to 5
        "target": "30%",
        "status": "✅ Exceeding target"
    },
    "assumption_3_conversation_depth": {
        "current": "2.1x",  # Data points vs forms
        "target": "3x",
        "status": "⚠️ Needs improvement"
    },
    "assumption_4_speed_retention": {
        "time": "1:45",   # Avg time to satisfaction
        "return": "38%",   # 7-day return rate
        "status": "✅ Meeting targets"
    }
}
```

---

## 🚦 Go/No-Go Decision Framework

### Week 2 Checkpoint
- [ ] Assumption 1: Hybrid quality test complete with 100+ tests
- [ ] Assumption 3: Conversation depth measured with 200+ users
- [ ] **Decision**: Continue if 2/2 assumptions validated

### Week 4 Final Decision  
- [ ] All 4 assumptions tested with statistical significance
- [ ] **GO if**: 3/4 assumptions clearly validated
- [ ] **PIVOT if**: 2/4 assumptions validated (adjust approach)
- [ ] **KILL if**: <2 assumptions validated

---

## 🎯 The Key Insight

**We're not building a complete product. We're building the minimum system needed to prove that hybrid intelligence + memory + conversation = better gift recommendations.**

Everything else can wait until we validate these core assumptions.