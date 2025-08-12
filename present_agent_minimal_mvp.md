# Present Agent: Minimal MVP Roadmap

## 🎯 Core Hypothesis
**People will trust an AI to help them find meaningful gifts if it asks the right questions about their relationships.**

## 🔥 Riskiest Assumptions to Test First

### Risk #1: Privacy vs Value Trade-off
**Assumption**: Users will share intimate relationship details with an AI
**Test**: Can we get users to describe their relationships naturally?
**Kill Criteria**: <20% share beyond basic demographics

### Risk #2: AI Cost Viability  
**Assumption**: We can deliver value at <$2 per recommendation
**Test**: Measure actual GPT-4 costs per successful recommendation
**Kill Criteria**: >$5 per recommendation with no optimization path

### Risk #3: Relationship Intelligence > Product Search
**Assumption**: Users prefer relationship-based recommendations over simple product search
**Test**: A/B test relationship questions vs product preferences
**Kill Criteria**: No measurable improvement in satisfaction

---

## 📦 The Absolute Minimum Product

### What We Ship (Week 1)
**One Channel**: Instagram DM only
**One Flow**: Text-based conversation
**One Database**: PostgreSQL only (no complex architecture yet)
**One AI**: GPT-4-turbo (cheaper than GPT-4.1)
**No Authentication**: Anonymous sessions only
**No Memory**: Each conversation starts fresh

### Core Experience (30 lines of prompting)
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

### Technical Stack (Minimal)
```python
# Entire MVP in ~500 lines of code
- FastAPI (1 webhook endpoint)
- PostgreSQL (3 tables: sessions, messages, recommendations)  
- OpenAI API (GPT-4-turbo)
- Instagram Webhook API
- Heroku (free tier)
```

---

## 🧪 Week-by-Week Assumption Testing

### Week 0: Manual Testing (No Code)
**Build**: Nothing - use your personal Instagram to manually chat with 10 friends
**Test**: Will people share relationship details via DM?
**Measure**: 
- How many share personal details?
- What questions unlock sharing?
- What makes them uncomfortable?
**Decision Point**: 
- ✅ Continue if >50% share meaningful details
- ❌ Kill if people refuse to engage

### Week 1: Wizard of Oz (Minimal Code)
**Build**: 
- Instagram webhook receiver (50 lines)
- Human-powered responses with templates
- Simple PostgreSQL logging

**Test**: Can we deliver value manually?
**Measure**:
- Time to find good recommendations
- User satisfaction (1-5 rating)
- What patterns emerge?

**Code Required**:
```python
# app.py - The entire MVP
from fastapi import FastAPI
import openai

app = FastAPI()

@app.post("/webhook")
async def instagram_webhook(data: dict):
    # Log message
    # Send to human operator dashboard
    # Return template response
```

**Decision Point**:
- ✅ Continue if satisfaction >3.5/5
- ❌ Pivot if we can't find good gifts manually

### Week 2: Basic AI Integration
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

### Week 3: Memory & Return Users
**Build**:
- User ID tracking (anonymous)
- Session persistence
- "Welcome back" experience

**Test**: Do users return? Does memory add value?
**Measure**:
- Return rate within 7 days
- Session completion with memory vs without
- User feedback on continuity

**Simple Implementation**:
```python
# Just store user_id -> recipient mappings
user_memory = {
    "user_id": "abc123",
    "recipients": ["mom", "girlfriend"],
    "last_recommendations": [...],
    "created_at": "2024-12-19"
}
```

**Decision Point**:
- ✅ Continue if return rate >20%
- ❌ Stay stateless if no improvement

### Week 4: Value Validation
**Build**:
- Add "Would you buy this?" question
- Track which recommendations users choose
- Simple affiliate link integration

**Test**: Will users actually purchase?
**Measure**:
- Intent to purchase rate
- Which recommendations get chosen
- Price sensitivity

**Decision Point**:
- ✅ Continue if >20% show purchase intent
- ❌ Pivot to different value prop

### Week 5: Scale Test
**Build**:
- Basic caching for common queries
- Rate limiting
- Error handling

**Test**: Can we handle 100 users/day profitably?
**Measure**:
- Infrastructure costs
- API costs at scale  
- Performance under load

**Decision Point**:
- ✅ Continue if unit economics work
- ❌ Need major architecture changes

### Week 6: Network Effect Test
**Build**:
- Track recommendation outcomes
- Find pattern: "Users like you also chose..."
- Test cross-user learning

**Test**: Do outcomes from User A improve User B's experience?
**Measure**:
- Recommendation acceptance rate with/without patterns
- Quality improvement over time

**Simple Implementation**:
```python
# Basic collaborative filtering
similar_users = find_similar(user_profile)
successful_gifts = get_successful_gifts(similar_users, occasion)
boost_recommendations(successful_gifts)
```

**Decision Point**:
- ✅ Build full platform if network effects exist
- ❌ Stay as simple recommendation tool

---

## 💰 Cost Model for 100 Users

### Per Conversation Costs
- GPT-4-turbo: ~$0.30 (assuming 3K tokens in, 1K out)
- Instagram API: Free
- Heroku: Free tier
- PostgreSQL: Free tier

### Assumptions to Validate
- Conversations average 5-7 messages
- 30% return within 30 days
- 20% show purchase intent
- 10% actually purchase (generating commission)

### Viability Threshold
**Break-even requirement**: 
- Need 10% purchase rate with $50 average order value
- $5 commission per purchase
- Cost per conversation: $0.30
- Need 1 purchase per 16 conversations to break even

---

## 🛑 Kill Criteria (When to Stop)

### Immediate Kills
1. **Instagram blocks bot**: Platform risk realized
2. **Nobody shares relationship details**: Core assumption false
3. **AI costs >$5 per conversation**: Economically unviable

### Week 4 Checkpoint Kills  
1. **<20% return rate**: No retention
2. **<10% purchase intent**: No monetization path
3. **Satisfaction <3/5**: Product doesn't deliver value

### Week 6 Final Decision
1. **No network effects measurable**: No competitive moat
2. **CAC >$50**: Unsustainable growth economics
3. **Manual operation still required**: Can't automate core loop

---

## 🚀 Success Criteria to Expand

### Minimum Metrics for Full Build
- **50+ daily active users**
- **>30% return within 7 days** 
- **>20% purchase intent**
- **<$2 cost per recommendation**
- **Network effects demonstrated**
- **Clear path to $10K MRR**

### What We Build Next (Only if successful)
1. Multi-database architecture (Neo4j, Vector DB)
2. WhatsApp/Messenger expansion
3. Persistent user profiles
4. Outcome tracking system
5. B2B enterprise offering

---

## 📝 Implementation Checklist (Week 1 Focus)

### Day 1-2: Setup
- [ ] Create Instagram Developer account
- [ ] Set up webhook endpoint on Heroku
- [ ] Create PostgreSQL database (3 tables)
- [ ] Write webhook handler (~50 lines)

### Day 3-4: Core Logic
- [ ] Write relationship extraction prompt
- [ ] Write gift recommendation prompt  
- [ ] Test with GPT-4-turbo playground
- [ ] Calculate token costs

### Day 5-7: Testing
- [ ] Test with 10 real users
- [ ] Measure sharing depth
- [ ] Track satisfaction scores
- [ ] Document conversation patterns

### Decision Point
- [ ] Go/No-Go decision based on data
- [ ] Document learnings
- [ ] Plan Week 2 or pivot

---

## 💡 The Key Insight

**Start with the conversation, not the technology.**

If users won't share relationship details in a simple chat, no amount of fancy databases or AI will save the product. Test the core human behavior first, then add complexity only where it demonstrably adds value.

**Total Week 1 Investment**:
- Time: 40 hours
- Cost: <$100 (OpenAI credits)
- Code: ~500 lines
- Learning: Invaluable

**Remember**: We're not building Present Agent in Week 1. We're testing whether Present Agent should exist at all.