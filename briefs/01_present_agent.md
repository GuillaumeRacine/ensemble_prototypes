# Present Agent - Product Brief

> AI gift recommendation app for ADHD adults. Deployed on Railway, 171K product catalog.
> Existing repo: `present-agent-v3-mar2026`

---

## Vision

An agentic gift concierge that owns the entire gifting journey -- from occasion trigger to recipient feedback -- using deep personal context and Claude Code workflows to deliver genuinely thoughtful gifts with zero cognitive load.

---

## Core Beliefs & Assumptions

### Agentic Shopping Thesis
- The next phase of internet/tech is **agents talking to agents**
- Users will have a personal agent on their device with permission levels they control (transparency, autonomy, data access)
- This enables **qualitative input** at scale -- not just clicks and filters but rich context sharing on an opt-in basis
- Human attention is fixed and scarce; recommendation vectors will multiply through agentic intermediaries
- The value accrues to whoever has the best context, not the most products

### Gifting vs. Self-Purchase
- Gifting is psychologically different from self-purchase -- different motivators, different anxiety profile
- Must consider psychological elements (social pressure, relationship dynamics, reciprocity) without being clinical
- The experience matters as much as the product itself
- Preserve everyone's feelings -- recipient feedback must be handled delicately

### Key Principle: Give Before You Ask
- Every interaction should follow a **give-ask-give-ask** cadence
- Start by delivering value before requesting commitment
- Make it easy to skip questions -- progressive disclosure, not interrogation

---

## Complete Gifter Journey (extracted)

### Phase 1: Trigger/Occasion
- Reminder that something is coming (birthday, anniversary, holiday)
- Could be: planned well in advance, day-of, or unplanned (life event, accident, surprise)
- Sources: calendar events, contact birthdays, manual input
- **Data integration**: Calendar mapping, contacts CRM, email scanning for event mentions

### Phase 2: Person Context
- Facts: who they are, relationship to gifter
- Interests: hobbies, preferences, style
- Past gifts and feedback on those (if any)
- Auto-memory of the person that builds over time
- External research: find more about what they like through other means
- **Result**: Well-researched, cohesive view of the recipient

### Phase 3: Search Parameters
- Rough budget (guidelines, not hard rules)
- Person's preferences from Phase 2
- Occasion type and formality level
- Narrow from unlimited choice to **3-5 best options**

### Phase 4: Idea Maze
- Ideas start abstract, need to funnel down to purchasable products
- Some high-level ideas won't work -- need graceful pivoting
- Consider: shipping time, delivery presentation, tracking, failure modes
- All-in cost visibility (product + shipping + wrapping)

### Phase 5: Compare & Decide
- Compare options across dimensions
- Check availability, delivery windows, reviews
- Show total cost transparently

### Phase 6: Purchase
- Buy the chosen item
- Decide delivery method: ship direct vs. concierge service

### Phase 7: Card
- Virtual or physical card
- Make it "the best card ever" -- AI-assisted personalization
- Could be an easier entry vector for the product

### Phase 8: Delivery Experience
- Concierge service: gift + card + delivery experience as a bundle
- Regional/local courier integration (Instacart-style A-to-B)
- Photo of delivery as memory
- Recipient gets a flyer inviting them into the platform

### Phase 9: Feedback Loop
- Recipient reports back (delicately handled)
- User learns from it
- System learns from it
- Feeds back into person context for next time

---

## Data Integration Points

| Source | What It Provides |
|--------|-----------------|
| Contacts/CRM | Names, relationships, birthdays |
| Calendar | Upcoming occasions, events |
| Email | Event mentions, order history |
| Past interactions | Gift history, feedback, preferences |
| Audio input | Hold-to-talk context sharing (key UX feature) |
| Photos | Visual context about recipient |

### Audio-First Input
- **Critical feature**: Let users hold a button and talk instead of type
- Send audio note explaining context about the person
- Anyone can use this -- lower friction than typing
- ADHD-friendly: dump context verbally

---

## Commerce & Distribution

### Shopify Store
- Build own Shopify store for Present Agent
- Makes products discoverable by other agents (agentic web)
- Control the full transaction loop (don't send users to external pages)

### Business Model Exploration
- Dropshipping / centralized model hybrid
- Payment processing and courier setup
- Own the end-to-end experience (key: don't lose user to external sites)

### Onboarding
- Product pages should funnel into app install
- Claude Code onboarding: what is the ideal first experience?
- How do users first encounter and start using the product?

---

## Technical Architecture Ideas

- Claude Code workflows as the interaction layer
- Opt-in context sharing with permission levels
- Auto-embed data: contacts, CRM, dates, calendars, emails
- Map recipient "clusters" from available data
- Progressive context building (each interaction adds data)
- Experiment framework: test recommendations, learn from what doesn't work

---

## Open Questions

1. How to handle the abstract-to-concrete idea funnel gracefully?
2. What's the minimum viable concierge service?
3. How to onboard users who don't use Claude Code?
4. Regional courier partnerships -- build or buy?
5. Card as standalone product / entry point?
6. How to make feedback feel safe for recipients?

---

## Issues to Create

- [ ] Full gifting journey UX flow (9 phases)
- [ ] Audio input / hold-to-talk feature
- [ ] Person context auto-memory system
- [ ] Calendar + contacts data integration
- [ ] Shopify store setup and product feed
- [ ] Card generation (virtual + physical)
- [ ] Concierge delivery service design
- [ ] Recipient feedback loop
- [ ] Onboarding flow design
- [ ] Give-ask-give interaction cadence
- [ ] Agent-to-agent discoverability (agentic web)
