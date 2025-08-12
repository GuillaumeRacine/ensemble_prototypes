# Present Agent: Claude Code Project Guide

## 🎯 Project Context

Present Agent is an AI-powered gift recommendation platform that transforms gift-giving through relationship intelligence. This document provides guidance for future Claude instances working on this project.

---

## 📋 Project Status & Objectives

### Current Phase: MVP Assumption Validation
We are testing 4 core assumptions with a 16-day implementation plan:
1. **Hybrid Intelligence > Pure Search** - Can our recommendation engine beat Amazon/Google?
2. **Memory Creates Compounding Value** - Does the system improve measurably with each interaction?
3. **Conversational UI Unlocks Sharing** - Will users share 3x more context via chat than forms?
4. **Fast + Learning = Retention** - Can we achieve <2 min satisfaction with >40% 7-day return?

### Key Success Metrics
- **Product-Market Fit**: NPS >50, >70% prefer our recommendations over alternatives
- **Unit Economics**: <$2 AI cost per recommendation, CAC/LTV <0.3
- **Technical Performance**: <500ms total pipeline, >85% relevance rate

---

## 🗂 File Organization & Purpose

### Product Development Files (Core Work)
- **`present_agent_product_brief.md`** - Complete business model canvas and strategy
- **`present_agent_data_model.md`** - 5-database hybrid architecture design
- **`mvp_assumption_validation.md`** - Framework for testing assumptions (START HERE)
- **`mvp_implementation_plan.md`** - 16-day coding roadmap (IMPLEMENTATION GUIDE)
- **`present_agent_minimal_mvp.md`** - Simplified approach for rapid testing
- **`present_agent_spec.md`** - Original technical specification

### Educational Reference
- **`technical_reference_guide.md`** - Combined technical research for your learning:
  - Why GPT-4 is optimal for this use case vs Claude/Gemini
  - Multi-stage recommendation system architecture
  - Context enrichment and data collection techniques
  - Performance benchmarks and implementation patterns

---

## 🛠 Custom Commands Available

Use these specialized commands for efficient product development:

### `/spec [product concept]`
Generates comprehensive product briefs following Marty Cagan's outcome-centric approach. Includes business model canvas, risk analysis, and 8-week validation plan.

### `/tech_research [technical challenge]`  
Conducts deep technical research including best practices, tool recommendations, scaling considerations, and production implementation guidance.

### `/improve_spec_prompt [baseline prompt]`
Optimizes prompts for better Claude Code usage with explicit tool guidance, quality gates, and evaluation scenarios.

---

## 🎯 Development Priorities

### Immediate Focus (Current Sprint)
1. **Validate Core Assumptions** - Use `mvp_assumption_validation.md` framework
2. **Implement MVP** - Follow `mvp_implementation_plan.md` day-by-day guide
3. **Test with Real Users** - Measure actual behavior, not intentions

### Technical Implementation Order
1. **Week 1-2**: Basic conversation engine + hard filtering (PostgreSQL only)
2. **Week 3-4**: AI integration (GPT-4) + hybrid recommendations 
3. **Week 5-6**: Memory system + user learning
4. **Week 7-8**: Experiment framework + go/no-go decision

### Key Architecture Decisions Made
- **LLM Choice**: GPT-4-turbo (optimal cost/performance for relationship understanding)
- **Database Strategy**: Start simple (PostgreSQL + Vector DB), scale to 5-database hybrid
- **Pipeline Target**: <500ms total (50ms filtering + 100ms semantic + 300ms ranking + 50ms optimization)

---

## 🚫 What NOT to Build Yet

Avoid these until core assumptions are validated:
- ❌ Payment processing or checkout flows
- ❌ Social sharing features  
- ❌ Multi-language support
- ❌ B2B enterprise features
- ❌ AR/VR experiences
- ❌ Advanced analytics dashboards

**Principle**: Only build what directly tests an assumption.

---

## 🔍 Key Context for AI Implementation

### Relationship Intelligence Focus
This is NOT a traditional e-commerce recommendation engine. We're building relationship intelligence that understands:
- Emotional context of gift-giving (apology vs celebration vs strengthening bonds)
- Cultural appropriateness across 100+ cultures
- Recipient personality and preferences from minimal context
- Gift exchange patterns and relationship dynamics

### Data Strategy
- **Privacy-first**: Explicit opt-in for data collection with clear value exchange
- **Progressive disclosure**: Start simple, build complexity naturally through conversation
- **Memory that matters**: Remember relationship context, not just product preferences
- **Network effects**: Each user's outcomes improve recommendations for similar relationships

### Conversation Design Philosophy
Natural language interaction that feels like talking to a thoughtful friend who:
- Asks smart follow-up questions
- Remembers important details
- Understands emotional subtext
- Provides reasoning for recommendations
- Learns from outcomes

---

## 📊 Success Criteria & Kill Criteria

### Continue Development If:
- ✅ 3/4 assumptions clearly validated
- ✅ Statistical significance in user behavior data
- ✅ Clear path to unit economics
- ✅ Technical feasibility proven

### Pivot/Kill If:
- ❌ <2 assumptions validated after 4 weeks
- ❌ Users won't share relationship context
- ❌ No measurable improvement over existing solutions
- ❌ AI costs >$5 per recommendation with no optimization path

---

## 🤝 Working with This Project

### For Coding Tasks
1. **Start with** `mvp_implementation_plan.md` for specific implementation guidance
2. **Reference** `technical_reference_guide.md` for architecture decisions and patterns
3. **Validate against** assumptions in `mvp_assumption_validation.md`
4. **Test early and often** with real user conversations

### For Product Questions
1. **Business context** in `present_agent_product_brief.md`
2. **Data model details** in `present_agent_data_model.md`  
3. **Technical specifications** in `present_agent_spec.md`

### For Research Tasks
Use custom commands (`/spec`, `/tech_research`, `/improve_spec_prompt`) for consistent, high-quality analysis following established frameworks.

---

## 💡 Guiding Principles

1. **Assumption-driven development** - Every feature tests a hypothesis
2. **User behavior over stated preferences** - Measure what people do, not what they say
3. **Relationship-first architecture** - Optimize for emotional connection, not transactions
4. **Progressive complexity** - Start simple, add sophistication based on validation
5. **Technical excellence** - Build for scale but validate assumptions first

---

## 🎯 The Ultimate Vision

We're building the emotional intelligence layer for human relationships in the digital age. Present Agent should become as essential as LinkedIn for professional networks, but for personal relationships.

**Success looks like**: Users naturally turn to Present Agent whenever they want to express care through gifting, because it understands their relationships better than they do themselves.

**Remember**: We're not building a gift app. We're building the operating system for human emotional connection through gifts.

---

*Last Updated: December 2024*  
*Next Milestone: MVP assumption validation complete*