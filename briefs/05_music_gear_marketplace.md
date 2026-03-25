# Music Gear Marketplace - Product Brief

> Agentic music gear shopping experience with full user context.
> New project.

---

## Vision

A context-aware music gear marketplace that aggregates listings from Reverb, Facebook Marketplace, Long & McQuade, and online retailers into a single view -- with deep user context (playing style, owned instruments, research history) powering better discovery, comparison, and trust.

---

## Pain Points with Current Solutions (Reverb, etc.)

| Problem | Impact |
|---------|--------|
| No context on user's playing, instruments, research | Generic recommendations |
| No cross-platform comparison | Fragmented shopping |
| Shipping cost hidden until checkout | Can't compare all-in cost |
| Fake listings exist | Trust erosion |
| No custom parts market aggregation | Missed opportunity |
| No lifecycle beyond purchase | No courses, bands, community |

---

## Core Features

### 1. Aggregated Listings
- Pull from: Reverb, Facebook Marketplace, Long & McQuade, other online retailers
- Unified view of all available gear
- Clearly detailed and **augmented with extra data** (specs, reviews, history, market price)
- Full view of all instruments and gear in one place

### 2. User Context System
- Playing style and skill level
- Instruments currently owned
- Research history and saved items
- Past purchases and reviews
- Audio clips of playing
- Photos of gear
- **Auto-memory** that builds over time

### 3. All-In Cost Comparison
- Product price + shipping + taxes + duties
- Compare apples-to-apples across platforms
- Show cheapest way to get it to you (pickup vs. ship)
- Transparent from the start (not hidden until checkout)

### 4. Trust Layer
- **Fake listing detection** via Reverb API and pattern matching
- Flag suspicious listings automatically
- Trust scores for sellers
- Extra verification layer users don't get from Reverb alone

### 5. Custom Parts Market
- Big underserved market
- Aggregate custom parts listings
- Help users find compatible parts for their instruments

### 6. Music Journey Beyond Gear
- Courses and learning resources
- Find a band to practice with
- Sell your own gear
- Gear research tools
- Full lifecycle, not just transactions

---

## Commerce Layer

### Shopify Store
- Own Shopify store for direct sales
- Load all photos, descriptions, inventory
- Tool/ecosystem to drive transactions on-site
- Control the end-to-end experience

### Acquisition Channels
| Channel | Approach |
|---------|----------|
| Existing listings | Appear alongside Reverb/FB results |
| Music stores | Direct channel partnership (Long & McQuade, etc.) |
| Word of mouth | Better experience drives referrals |
| Agentic web | Other agents discover store |

### User Onboarding
- Cloud Code / agentic onboarding
- Personal, guided first experience
- Build context from first interaction

---

## Technical Architecture

### Data Pipeline
```
Reverb API ->
Facebook Marketplace scrape ->    Unified
Long & McQuade scrape ->          Listing
Other retailers ->                Database
```

### User Profile
```
Playing style + instruments owned + research history
+ audio clips + photos + past purchases
-> Context Engine -> Personalized recommendations
```

### Trust Engine
```
Listing data -> Pattern detection -> Fake score
Seller history -> Trust score
Price comparison -> Market value check
```

---

## Issues to Create

- [ ] Multi-source listing aggregator (Reverb, FB, L&M, retailers)
- [ ] Unified listing data model with augmented specs
- [ ] User context system (instruments, style, history)
- [ ] All-in cost calculator (price + shipping + fees)
- [ ] Fake listing detection engine
- [ ] Shopify store setup for direct sales
- [ ] Custom parts marketplace integration
- [ ] Music journey features (courses, bands, community)
- [ ] Agentic onboarding flow
- [ ] Cross-platform price comparison view
- [ ] Audio/photo context capture for user profiles
