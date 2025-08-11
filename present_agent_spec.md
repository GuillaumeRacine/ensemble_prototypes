# Present Agent: MVP Prototype Specification

## Problem Statement

Gift-giving creates stress for millions. People struggle to find meaningful gifts, remember occasions, and shop within their values. We need to validate if an AI assistant can make gifting truly easy and thoughtful.

## Solution Vision

A lightweight AI chatbot that starts simple - learning about one user and helping them find one great gift. Ship weekly, learn fast, iterate based on real user feedback.

## MVP Scope - Weekly Iterations

### Week 1: Basic Chat Interface ✅
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

### Week 2: AI-Powered Recommendations 🤖
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

### Week 3: User Memory 🧠
**Ship:** Bot remembers users between conversations
**Features:**
- Simple user profiles (name, past recipients)
- "Welcome back" experience
- Reference previous gift searches

**Success Metric:** 30% returning users

**Implementation:**
```
  ├── models.py          # User, Recipient models
  └── memory.py          # Simple PostgreSQL storage
```

### Week 4: Values-Based Search 🌱
**Ship:** Filter by user values
**Features:**
- Add budget constraints
- Filter by values (eco-friendly, local, secondhand)
- Explain why each suggestion matches

**Success Metric:** Users engage with values filters

**Implementation:**
```
  └── filters.py         # Value-based filtering logic
```

### Week 5: Multi-Channel 📱
**Ship:** Add ONE more platform
**Features:**
- WhatsApp or Messenger integration
- Unified backend for both channels
- Same experience across platforms

**Success Metric:** 20% of users on new platform

### Week 6: Gift Tracking 📝
**Ship:** Help users stay organized
**Features:**
- Save gift ideas for later
- Set occasion reminders
- "What did I get them last year?"

**Success Metric:** Users save gifts for future

### Week 7: Social Proof 🌟
**Ship:** Build trust through community
**Features:**
- "Popular gifts for [occasion]"
- Anonymous success stories
- Quick feedback after gifting

**Success Metric:** Improved suggestion acceptance rate

### Week 8: Polish & Scale 🚀
**Ship:** Production-ready MVP
**Features:**
- Error handling and edge cases
- Performance optimization
- Analytics dashboard
- User feedback collection

**Success Metric:** Ready for 100+ daily users

## Technical Approach - Keep It Simple

### Minimal Stack
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

### Core Data Model (Start Simple)
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

## User Testing Protocol

### Weekly User Interviews (5 users minimum)
1. **Onboarding:** How was your first experience?
2. **Quality:** Were the suggestions relevant?
3. **Speed:** Was it faster than your usual process?
4. **Trust:** Would you buy these gifts?
5. **Return:** Will you use it again?

### Key Metrics to Track
- Conversation completion rate
- Time to recommendation
- Suggestion acceptance rate
- Return user rate
- Platform preference

## Risk Mitigation - Start Small

| Risk | Simple Solution |
|------|-----------------|
| Complex AI responses | Use templated responses with AI fill-ins |
| Platform restrictions | Start with one platform, validate, then expand |
| Data privacy | Minimal data collection, clear consent |
| Scaling issues | Cap at 100 users initially |
| Poor recommendations | Human review queue for quality |

## Launch Strategy

### Week 1-4: Friends & Family Alpha
- 10-20 close users
- Daily feedback
- Rapid iteration

### Week 5-6: Private Beta
- 50 users from waitlist
- Instagram/Discord community
- Weekly surveys

### Week 7-8: Public Beta
- Open access with "Beta" label
- Feedback widget in chat
- Public roadmap

## Success Criteria for Full Build

Before investing in full implementation:
- [ ] 100+ active users
- [ ] 40% week-over-week retention
- [ ] 4.5+ star rating
- [ ] Clear monetization path
- [ ] Platform approval for scaling

## Next Immediate Steps

1. **Today:** Set up Meta Developer account
2. **Tomorrow:** Deploy basic webhook endpoint
3. **This Week:** Ship Week 1 prototype
4. **Next Week:** Get first 10 users testing

---

*Remember: Ship small, learn fast, iterate based on real user needs. Every week should produce something users can actually try.*