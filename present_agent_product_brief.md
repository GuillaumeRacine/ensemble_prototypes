# Present Agent - Product Brief

## 1. Problem

**Description:** Gift-givers waste hours searching for meaningful presents, often defaulting to generic choices that fail to express genuine care.

**Why it matters:**
- 78% of people report gift-giving anxiety before major occasions
- Average person spends 10+ hours annually searching for gifts
- $75B in unwanted gifts returned annually (US)
- Relationships suffer when gifts miss the mark

**Current alternatives:**
- **Amazon/E-commerce browsing:** Overwhelming choice paralysis, no personalization
- **Gift guides/blogs:** Generic, not tailored to specific relationships
- **Asking directly:** Ruins surprise, feels impersonal
- **Gift cards:** Lazy perception, no emotional value

## 2. Solution

**Concept:** AI-powered chat assistant that learns about gift recipients through natural conversation, delivering hyper-personalized recommendations in under 3 minutes.

**Differentiation:**
- Learns relationships over time (not one-off transactions)
- Values-based filtering (eco, local, secondhand)
- Native in messaging apps where users already are
- Remembers past gifts to avoid duplicates

**Intended impact:** Transform gift-giving from stressful obligation to joyful expression of care.

## 3. Audience

**Ideal Customer:**
- Age 25-45, urban/suburban
- Active on Instagram/WhatsApp
- Gives 5+ gifts annually
- Values relationships but time-constrained
- Willing to spend $30-200 per gift
- Cares about sustainability/ethics

**Exclusions:**
- Last-minute shoppers wanting same-day delivery
- Luxury gift buyers ($500+)
- Corporate/bulk gift buyers
- Users without smartphones

**Identification:**
- Follow lifestyle/wellness accounts on Instagram
- Engage with sustainable brands
- Search Pinterest for gift ideas
- Subscribe to services like Stitch Fix

**Service Approach:**
- Proactive reminders before occasions
- Quick check-ins post-gift for feedback
- Seasonal gift guides based on their values
- 24/7 availability for spontaneous needs

## 4. User Experience

**Primary user journey:**
1. Discovers via Instagram ad → DMs Present Agent
2. Brief onboarding (name, first gift need)
3. Describes recipient in natural language
4. Receives 3 curated suggestions with reasoning
5. Saves favorite for later or gets purchase link
6. Returns for next occasion with context retained

**Core interactions:**
- Natural language chat (no forms/menus)
- Visual product cards with descriptions
- One-tap save/share functionality
- Quick feedback thumbs up/down

**Edge cases:**
- Group gifts coordination
- International shipping needs
- Budget constraints mid-conversation
- Switching between platforms (Instagram → WhatsApp)

## 5. Technical Implementation

**Architecture outline:**
```
User → Messaging Platform → Webhook Handler → AI Service
                                    ↓
                            User Context DB ← Redis Cache
```

**Complexity points:**
- Natural language understanding across cultures/languages
- Real-time product inventory integration
- Cross-platform conversation continuity
- Scaling AI costs with growth

**Dependencies:**
- Meta Business Platform approval
- OpenAI API (GPT-4)
- Product catalog partnerships
- Payment processor integration

## 6. Limitations

**Known constraints:**
- $5,000 initial budget
- Solo developer for first 8 weeks
- Meta API rate limits (200 req/sec)
- No direct purchase capability initially

**Trade-offs:**
- Single language (English) to start
- No voice interface
- Limited to 3 suggestions per query
- Manual product catalog updates

## 7. Risks & Assumptions

### 7.1 Desirability

**Assumption 1:** Users trust AI for personal gift recommendations
- **Risk if false:** Zero adoption, product fails
- **Experiment:** Week 1 - Test with 20 users using Wizard of Oz prototype

**Assumption 2:** 3-minute interaction is fast enough
- **Risk if false:** Users abandon mid-conversation
- **Experiment:** Week 2 - Time trials with real AI, measure completion rates

**Assumption 3:** Users want to be remembered across sessions
- **Risk if false:** Privacy concerns kill retention
- **Experiment:** Week 3 - A/B test memory feature opt-in rates

### 7.2 Viability

**Assumption 1:** Users will pay 10% commission on purchases
- **Risk if false:** No revenue model
- **Experiment:** Week 4 - Test willingness to pay with mock checkout

**Assumption 2:** CAC < $20 via Instagram ads
- **Risk if false:** Unprofitable growth
- **Experiment:** Week 5 - Run $500 ad campaign, measure conversions

**Assumption 3:** 40% monthly retention achievable
- **Risk if false:** Constant reacquisition costs
- **Experiment:** Week 6 - Cohort analysis of first 100 users

### 7.3 Feasibility

**Assumption 1:** OpenAI API reliable enough for production
- **Risk if false:** Poor user experience
- **Experiment:** Week 2 - Stress test with 100 concurrent conversations

**Assumption 2:** Meta won't restrict/ban our use case
- **Risk if false:** Platform risk
- **Experiment:** Week 1 - Submit for review, test limits

**Assumption 3:** Can handle multi-platform conversations
- **Risk if false:** Fragmented experience
- **Experiment:** Week 5 - Test unified backend across platforms

## 8. Prototype & Learning Plan

### Week 1: Wizard of Oz Testing
- **Build:** Instagram DM with human-powered responses
- **Test:** Desirability - Do users engage?
- **Measure:** Completion rate >50%, satisfaction >4/5
- **Next if true:** Add AI | **If false:** Pivot concept

### Week 2: AI Integration
- **Build:** GPT-4 powered recommendations
- **Test:** Speed & quality acceptable?
- **Measure:** <3 min interactions, relevance score >70%
- **Next if true:** Add memory | **If false:** Improve prompts

### Week 3: User Memory
- **Build:** Session persistence, user profiles
- **Test:** Privacy vs personalization balance
- **Measure:** Opt-in >60%, return rate >30%
- **Next if true:** Add values | **If false:** Anonymous mode

### Week 4: Values & Monetization
- **Build:** Eco/local filters, commission test
- **Test:** Values matter? Will they pay?
- **Measure:** Filter usage >40%, payment acceptance >20%
- **Next if true:** Scale test | **If false:** Try subscription

### Week 5: Multi-Channel & Marketing
- **Build:** WhatsApp integration, ad campaign
- **Test:** CAC viable? Platform unity works?
- **Measure:** CAC <$20, cross-platform retention
- **Next if true:** Gift tracking | **If false:** Focus single platform

### Week 6: Gift Management
- **Build:** Save gifts, reminders, history
- **Test:** Organizational features drive retention?
- **Measure:** Feature adoption >50%, MAU increase
- **Next if true:** Social proof | **If false:** Simplify

### Week 7: Social & Trust
- **Build:** Reviews, popular gifts, success stories
- **Test:** Social proof improves conversion?
- **Measure:** Suggestion acceptance +20%
- **Next if true:** Polish | **If false:** Direct recommendations

### Week 8: Production Ready
- **Build:** Error handling, analytics, feedback loops
- **Test:** Ready for 1000 users?
- **Measure:** Uptime >99%, response time <200ms
- **Next:** Launch or iterate based on learnings

### Success Criteria for Continued Investment:
- **Desirability:** 100+ active users, NPS >50
- **Viability:** CAC/LTV ratio <0.3, clear path to $10K MRR
- **Feasibility:** <$500/month operating costs, 2 hrs/week maintenance

### Kill Criteria:
- Retention <20% after week 4
- CAC >$50 consistently
- Platform restrictions prevent core functionality
- User feedback consistently negative on core value prop