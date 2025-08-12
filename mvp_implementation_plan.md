# Present Agent MVP: 16-Day Implementation Plan

## 🎯 Goal: Validate 4 Core Assumptions in 16 Days

### What We're Building
A minimal chat-based gift recommendation system that proves:
1. Hybrid recommendations beat pure search
2. Memory creates compounding value  
3. Chat unlocks personal sharing
4. Fast + learning = retention

---

## 📅 Day-by-Day Coding Plan

### Days 1-2: Project Foundation
```bash
# Terminal commands to run
mkdir present_agent_mvp && cd present_agent_mvp
python -m venv venv && source venv/bin/activate
pip install fastapi uvicorn openai psycopg2-binary sqlalchemy python-dotenv pytest httpx

# Create project structure
touch .env requirements.txt README.md
mkdir -p app/{api,core,db,services,experiments}
```

**Day 1 Deliverables**:
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

**Day 2 Deliverables**:
```python
# app/db/models.py - Core data models
from sqlalchemy import Column, String, JSON, DateTime, Float
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

### Days 3-5: Conversation Engine
**Day 3: Basic Chat Flow**
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

**Day 4: Natural Question Generation**
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

**Day 5: Context Validation**
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
    
    def parse_budget(self, budget_str: str) -> Optional[tuple[float, float]]:
        # Parse various budget formats: "$50-100", "around 50", "under 100"
        import re
        
        # Range: "$50-100"
        range_match = re.search(r'\$?(\d+)\s*-\s*\$?(\d+)', budget_str)
        if range_match:
            return float(range_match.group(1)), float(range_match.group(2))
        
        # Around: "around $50"
        around_match = re.search(r'around\s*\$?(\d+)', budget_str, re.I)
        if around_match:
            val = float(around_match.group(1))
            return val * 0.8, val * 1.2
        
        # Under: "under $100"
        under_match = re.search(r'under\s*\$?(\d+)', budget_str, re.I)
        if under_match:
            val = float(under_match.group(1))
            return 0, val
        
        return None
```

### Days 6-8: Product Catalog & Hybrid Recommendation
**Day 6: Product Catalog Setup**
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
    
    def semantic_search(self, query_embedding: List[float], limit: int = 50) -> List[Dict]:
        # Find products with similar embeddings
        # For MVP: Use pre-computed embeddings
        similarities = self.compute_similarities(query_embedding, self.embeddings)
        top_indices = similarities.argsort()[-limit:][::-1]
        return self.products.iloc[top_indices].to_dict('records')
```

**Day 7: Hybrid Recommender**
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
    
    def context_to_query(self, context: Dict) -> str:
        # Convert context to product search query
        parts = []
        
        if context.get('interests'):
            parts.extend(context['interests'])
        
        if context.get('occasion'):
            parts.append(f"{context['occasion']} gift")
        
        if context.get('relationship'):
            parts.append(f"for {context['relationship']}")
        
        return " ".join(parts)
    
    def rank_by_relationship(self, products: List[Dict], context: Dict) -> List[Dict]:
        # Use GPT to rank products by relationship appropriateness
        prompt = f"""
        Context: Shopping for {context.get('relationship')} for {context.get('occasion')}.
        Recipient interests: {context.get('interests')}
        
        Rank these products by appropriateness (1-10):
        {[p['name'] for p in products[:20]]}
        
        Return as JSON: {{"product_name": score}}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        scores = json.loads(response.choices[0].message.content)
        
        # Sort products by score
        for product in products:
            product['relationship_score'] = scores.get(product['name'], 5)
        
        return sorted(products, key=lambda x: x['relationship_score'], reverse=True)
```

**Day 8: Explanation Generation**
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

### Days 9-11: Memory System
**Day 9: User Memory Storage**
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
    
    def remember_recipient(self, user_id: str, context: Dict):
        # Check if recipient exists
        existing = self.db.query(Recipient).filter_by(
            user_id=user_id,
            name=context.get('recipient')
        ).first()
        
        if existing:
            # Update with new information
            existing.attributes = {
                **existing.attributes,
                **context.get('interests', {})
            }
        else:
            # Create new recipient profile
            recipient = Recipient(
                user_id=user_id,
                name=context.get('recipient'),
                relationship=context.get('relationship'),
                attributes={
                    'interests': context.get('interests'),
                    'age': context.get('age'),
                    'occasions': [context.get('occasion')]
                }
            )
            self.db.add(recipient)
    
    def get_user_context(self, user_id: str) -> Dict:
        # Retrieve all learned information
        recipients = self.db.query(Recipient).filter_by(user_id=user_id).all()
        sessions = self.db.query(Session).filter_by(user_id=user_id).order_by(
            Session.created_at.desc()
        ).limit(5).all()
        
        return {
            'recipients': [r.to_dict() for r in recipients],
            'recent_sessions': [s.to_dict() for s in sessions],
            'preferences': self.extract_preferences(sessions)
        }
```

**Day 10: Learning from Feedback**
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

def boost_preference(self, user_id: str, recommendation: Dict):
    # Increase weight for similar products
    product_type = recommendation['product']['category']
    price_range = recommendation['product']['price']
    
    # Store positive signal
    preference = {
        'type': 'positive',
        'category': product_type,
        'price_range': price_range,
        'timestamp': datetime.utcnow()
    }
    
    # This will influence future recommendations
    self.store_preference_signal(user_id, preference)
```

**Day 11: Memory-Enhanced Recommendations**
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

### Days 12-13: Experiment Framework
**Day 12: A/B Testing Setup**
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
        self.assignments = {}  # User -> variant mapping
        self.metrics = defaultdict(list)
    
    def assign_variant(self, user_id: str, experiment: str) -> str:
        # Consistent assignment for user
        key = f"{user_id}_{experiment}"
        
        if key not in self.assignments:
            variants = self.experiments[experiment]['variants']
            self.assignments[key] = random.choice(variants)
        
        return self.assignments[key]
    
    def track_metric(self, experiment: str, variant: str, metric: str, value: Any):
        key = f"{experiment}_{variant}_{metric}"
        self.metrics[key].append(value)
    
    def get_results(self, experiment: str) -> Dict:
        results = {}
        
        for variant in self.experiments[experiment]['variants']:
            variant_metrics = {}
            
            for metric in self.experiments[experiment]['metrics']:
                key = f"{experiment}_{variant}_{metric}"
                values = self.metrics.get(key, [])
                
                if values:
                    variant_metrics[metric] = {
                        'mean': sum(values) / len(values),
                        'count': len(values),
                        'values': values
                    }
            
            results[variant] = variant_metrics
        
        return results
```

**Day 13: Assumption Validation Tests**
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
    
    def validate_assumption_2_memory_value(self) -> Dict:
        """Test: Memory improves satisfaction over time"""
        # Compare session 1 vs session 5 satisfaction
        users_with_memory = self.get_users_with_multiple_sessions()
        
        improvements = []
        for user in users_with_memory:
            first_session = self.get_user_session(user, 1)
            fifth_session = self.get_user_session(user, 5)
            
            if first_session and fifth_session:
                improvement = (
                    fifth_session['satisfaction'] - first_session['satisfaction']
                ) / first_session['satisfaction']
                improvements.append(improvement)
        
        avg_improvement = sum(improvements) / len(improvements) if improvements else 0
        
        return {
            'pass': avg_improvement > 0.3,  # >30% improvement
            'improvement_rate': avg_improvement,
            'sample_size': len(improvements)
        }
```

### Days 14-15: API & Testing Interface
**Day 14: REST API**
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
        
        # Track metrics
        experiments.track_metric(
            'hybrid_vs_search',
            variant,
            'time_to_recommendation',
            time.time() - start_time
        )
        
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

@router.post("/feedback")
async def feedback(user_id: str, session_id: str, feedback: Dict):
    # Learn from feedback
    memory_system.learn_from_feedback(session_id, feedback)
    
    # Track for experiments
    experiments.track_metric(
        'memory_value',
        'with_memory',
        'feedback_received',
        1
    )
    
    return {"status": "learned", "impact": "will improve future recommendations"}
```

**Day 15: Simple Test UI**
```html
<!-- app/static/test_interface.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Present Agent MVP Test</title>
    <style>
        .chat-container {
            max-width: 600px;
            margin: 50px auto;
            font-family: Arial, sans-serif;
        }
        .messages {
            height: 400px;
            overflow-y: scroll;
            border: 1px solid #ccc;
            padding: 20px;
            margin-bottom: 20px;
        }
        .message {
            margin: 10px 0;
            padding: 10px;
            border-radius: 5px;
        }
        .user { background: #e3f2fd; text-align: right; }
        .bot { background: #f5f5f5; }
        .recommendation {
            border: 1px solid #ddd;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .feedback-buttons {
            margin-top: 10px;
        }
        button {
            padding: 5px 15px;
            margin: 0 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <h1>Present Agent - Gift Recommendation Test</h1>
        <div class="messages" id="messages"></div>
        <input type="text" id="input" placeholder="Tell me who you're shopping for..." style="width: 100%; padding: 10px;">
        <div id="metrics" style="margin-top: 20px; padding: 10px; background: #f0f0f0;">
            <strong>Test Metrics:</strong>
            <div>Time to recommendation: <span id="time">-</span></div>
            <div>Messages exchanged: <span id="msg-count">0</span></div>
            <div>User ID: <span id="user-id">-</span></div>
        </div>
    </div>

    <script>
        let userId = localStorage.getItem('userId');
        let startTime = Date.now();
        let messageCount = 0;
        
        async function sendMessage() {
            const input = document.getElementById('input');
            const message = input.value;
            if (!message) return;
            
            // Display user message
            addMessage(message, 'user');
            input.value = '';
            messageCount++;
            
            // Send to API
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    message: message,
                    user_id: userId
                })
            });
            
            const data = await response.json();
            userId = data.user_id;
            localStorage.setItem('userId', userId);
            document.getElementById('user-id').textContent = userId;
            
            // Display response
            if (data.type === 'recommendations') {
                displayRecommendations(data.content);
                const timeToRec = ((Date.now() - startTime) / 1000).toFixed(1);
                document.getElementById('time').textContent = timeToRec + 's';
            } else {
                addMessage(data.content, 'bot');
            }
            
            document.getElementById('msg-count').textContent = messageCount;
        }
        
        function addMessage(text, sender) {
            const div = document.createElement('div');
            div.className = `message ${sender}`;
            div.textContent = text;
            document.getElementById('messages').appendChild(div);
            div.scrollIntoView();
        }
        
        function displayRecommendations(recommendations) {
            const container = document.getElementById('messages');
            
            recommendations.forEach((rec, index) => {
                const div = document.createElement('div');
                div.className = 'recommendation';
                div.innerHTML = `
                    <h3>${rec.product.name}</h3>
                    <p>$${rec.product.price}</p>
                    <p><em>${rec.explanation}</em></p>
                    <div class="feedback-buttons">
                        <button onclick="sendFeedback(${index}, 'love')">❤️ Love it</button>
                        <button onclick="sendFeedback(${index}, 'maybe')">🤔 Maybe</button>
                        <button onclick="sendFeedback(${index}, 'no')">👎 No thanks</button>
                    </div>
                `;
                container.appendChild(div);
            });
        }
        
        async function sendFeedback(index, reaction) {
            await fetch('/api/feedback', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    user_id: userId,
                    session_id: 'current',
                    feedback: {
                        index: index,
                        reaction: reaction,
                        satisfied: reaction === 'love',
                        time_seconds: (Date.now() - startTime) / 1000
                    }
                })
            });
            
            if (reaction === 'love') {
                addMessage('Great! I\'ll remember this for next time.', 'bot');
            }
        }
        
        document.getElementById('input').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });
    </script>
</body>
</html>
```

### Day 16: Launch & Monitoring
**Final Day: Deployment & Metrics**
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
    
    def check_hybrid_quality(self) -> Dict:
        validator = AssumptionValidator(self.experiments)
        result = validator.validate_assumption_1_hybrid_quality()
        
        return {
            'status': '✅' if result['pass'] else '❌',
            'current': f"{result['preference_rate']*100:.1f}%",
            'target': '70%',
            'sample_size': result['sample_size'],
            'needs': max(0, 100 - result['sample_size'])  # How many more tests needed
        }
    
    def check_speed_retention(self) -> Dict:
        # Average time to satisfaction
        sessions = self.db.query(Session).filter(
            Session.time_to_satisfaction.isnot(None)
        ).all()
        
        avg_time = sum(s.time_to_satisfaction for s in sessions) / len(sessions) if sessions else 0
        
        # 7-day return rate
        week_ago = datetime.utcnow() - timedelta(days=7)
        users_week_ago = self.db.query(User).filter(
            User.created_at <= week_ago
        ).all()
        
        returned_users = [
            u for u in users_week_ago 
            if self.db.query(Session).filter(
                Session.user_id == u.id,
                Session.created_at > week_ago
            ).count() > 0
        ]
        
        return_rate = len(returned_users) / len(users_week_ago) if users_week_ago else 0
        
        return {
            'status': '✅' if avg_time < 120 and return_rate > 0.4 else '❌',
            'time_to_satisfaction': f"{avg_time:.0f}s",
            'return_rate': f"{return_rate*100:.1f}%",
            'targets': '<120s and >40%'
        }

# Deployment script
if __name__ == "__main__":
    import uvicorn
    
    # Start the API
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
```

---

## 🚀 Launch Checklist

### Pre-Launch (Day 15)
- [ ] Load 10,000 products into catalog
- [ ] Test conversation flow with 10 internal users
- [ ] Verify all metrics are being tracked
- [ ] Set up error monitoring

### Launch Day (Day 16)  
- [ ] Deploy to Heroku/Railway
- [ ] Share test link with 50 beta users
- [ ] Monitor metrics dashboard hourly
- [ ] Fix critical bugs immediately

### Success Criteria Check (Day 16 EOD)
- [ ] 100+ test conversations completed
- [ ] All 4 assumptions have initial data
- [ ] No critical errors in production
- [ ] Clear go/no-go decision possible

---

## 📊 Expected Outcomes

By Day 16, we'll know:
1. **Do hybrid recommendations beat search?** (Yes/No with data)
2. **Does memory improve satisfaction?** (% improvement measured)
3. **Will people share via chat?** (Data points collected vs forms)
4. **Is it fast enough and sticky?** (Time + return rate measured)

**Investment**: 16 days, ~1000 lines of code, $500 in API costs
**Decision**: Clear data on whether to proceed, pivot, or kill

The key: **Every line of code directly tests an assumption. Nothing more.**