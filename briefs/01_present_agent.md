# Present Agent — Technical Architecture & Product Documentation

> AI gift concierge that owns the entire gifting journey. 171K products, 236K reviews, Shopify commerce, Claude Code CLI skills.

**Repo:** `present-agent-v3-mar2026` (private)
**Store:** `xrbthg-vv.myshopify.com` (Shopify Basic, CAD)
**Status:** Functional prototype, ready for user testing

---

## Vision

An agentic gift concierge that owns the entire gifting journey -- from occasion trigger to recipient feedback -- using deep personal context and Claude Code workflows to deliver genuinely thoughtful gifts with zero cognitive load.

### Core Thesis: Agentic Commerce

The next phase of e-commerce is **agents talking to agents**. The user's personal agent (Claude Code) already knows their contacts, calendar, relationships, and preferences. Present Agent is the gift expert. Neither interrogates the user -- they exchange context programmatically.

```
USER'S AGENT                              PRESENT AGENT
┌─────────────────────┐                   ┌─────────────────────┐
│ Knows:              │                   │ Knows:              │
│ - All contacts      │ ── context ──→    │ - 171K products     │
│ - Calendar events   │    exchange       │ - 236K reviews      │
│ - Relationships     │                   │ - Gift intelligence │
│ - Past conversations│ ←── recs ────     │ - What works/doesn't│
│ - Preferences       │                   │                     │
└─────────────────────┘                   └─────────────────────┘
```

The value accrues to whoever has the **best context**, not the most products.

### Design Principles

1. **Give before you ask** -- every interaction delivers value before requesting input
2. **The best onboarding is no onboarding** -- use context the agent already has
3. **ADHD as design constraint** -- minimize questions, maximize value per turn, close loops
4. **Gift psychology over product matching** -- gifting is emotionally different from self-purchase

---

## Architecture

### System Overview

```
/remind (calendar)
    │
    v
/gift (chat → recommend)
    │
    v
/buy (Shopify cart → checkout)
    │
    v
Webhooks (order tracking)
    │
    v
/feedback (learning loop)
    │
    └──→ Context accumulation ──→ Better next recommendation
```

### Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 14 (App Router) |
| Database | SQLite (better-sqlite3, WAL mode) |
| Recommendation LLM | OpenAI gpt-4o-mini (swappable) |
| Chat LLM | Gemini 2.5 Flash |
| Commerce | Shopify (Storefront API + Admin API) |
| CLI Interface | Claude Code skills (`/gift`, `/buy`, `/remind`) |
| Hosting | Railway (production), localhost (dev) |
| Auth | Google OAuth (contacts + calendar access) |

### Data Flow

```
Shopify Store Crawl (282 stores)
    → 171,450 products in SQLite
    → Claude Sonnet enrichment (gift intelligence: psychological fit, relationship fit, occasions, traits)
    → Okendo API + Firecrawl (236,731 customer reviews)
    → OpenAI review intelligence (themes, gift signals, quality notes)
    → OpenAI gift dimensions (suitability score, relationships, occasions, reactions, uniqueness)
    → Shopify sync (products + metafields → checkout-ready)
    → Recommendation engine (prefilter + LLM ranking + social proof)
    → User gets 3 personalized picks with real customer voices
```

---

## Data Pipeline (5 layers)

### Layer 1: Product Catalog
**Source:** Shopify stores' public `/products.json` API
**Script:** `scripts/crawl-stores.ts`
**Output:** 171,450 products from 282 stores

| Field | Source |
|-------|--------|
| name, brand, price | Shopify API |
| description, images | Shopify API |
| category | Keyword classification |
| buy_url | Constructed from handle |

### Layer 2: Gift Intelligence (LLM Enrichment)
**Source:** Product metadata → Claude Sonnet
**Script:** `scripts/enrich-products.ts` (50 concurrent workers, ~5K products/min)
**Coverage:** 171,450 (100%)

| Field | What It Is |
|-------|-----------|
| `psychological_fit` | ["practical", "thoughtful", "playful", "luxurious", "sentimental", "adventurous"] |
| `relationship_fit` | ["partner", "parent", "child", "friend", "professional", "acquaintance"] |
| `recipient_traits` | Free-form tags: ["coffee", "outdoors", "minimalist", ...] |
| `occasion_fit` | ["birthday", "mothers_day", "christmas", ...] (14 canonical values) |
| `effort_signal` | "low_effort" / "moderate_effort" / "high_effort" |
| `price_tier` | "token" / "budget" / "moderate" / "premium" / "luxury" |
| `usage_signal` | "She'll reach for this every morning" |
| `what_this_says` | "This says: 'I notice your daily rituals'" |

### Layer 3: Customer Reviews
**Source:** Okendo API (free, unauthenticated) + Firecrawl (JS-rendered pages)
**Scripts:** `scripts/scrape-reviews.ts`, `scripts/scrape-reviews-firecrawl.ts`
**Coverage:** 12,652 products with reviews, 236,731 total reviews

| Field | What It Is |
|-------|-----------|
| `review_rating` | 1.0-5.0 aggregate |
| `review_count` | Total reviews |
| `review_breakdown` | {"5": 32314, "4": 3235, "3": 1654, ...} |
| `review_excerpts` | Top 5 customer quotes with reviewer name, verified status, date |
| `review_sentiment` | "overwhelmingly_positive" / "positive" / "mixed_positive" / "mixed" |

**Okendo stores (free API, unlimited):** burga.com, toddsnyder.com, astridandmiyu.com, ridgewallet.com, gorjana.com

**Key discovery:** Okendo's API at `api.okendo.io/v1/stores/{subscriberId}/products/{productId}/reviews` is public and unauthenticated. One Firecrawl scrape per store to extract the subscriber ID, then unlimited free review access.

### Layer 4: Review Intelligence
**Source:** Review text → OpenAI gpt-4o-mini
**Script:** `scripts/enrich-from-reviews.ts`
**Coverage:** 9,686 products (those with 5+ reviews)

| Field | What It Is |
|-------|-----------|
| `review_themes` | ["daily wear staple", "great for stacking", "runs small"] |
| `gift_signals` | ["popular birthday gift", "great for moms", "ideal for special occasions"] |
| `quality_notes` | "Chain can be snug for second piercings" |

### Layer 5: Gift Dimensions
**Source:** Product metadata + reviews → OpenAI gpt-4o-mini
**Script:** `scripts/enrich-gift-dimensions.ts`
**Coverage:** 171,020 products (99.7%)

| Field | What It Is |
|-------|-----------|
| `gift_suitability_score` | 0.0-1.0 (how good is this as a gift?) |
| `gift_proven` | Boolean: real people gave this as a gift successfully |
| `relationships_mentioned` | {"wife": 4, "mother": 3, "friend": 2} |
| `occasions_mentioned` | {"birthday": 5, "christmas": 3} |
| `recipient_reactions` | {"loved_it": 8, "daily_use": 5} |
| `fit_notes` | "true_to_size" / "runs_small" / "runs_large" / "n/a" |
| `unboxing_experience` | "premium" / "good" / "basic" |
| `regift_risk` | "low" / "medium" / "high" |
| `price_perception` | "great_value" / "good_value" / "fair" / "expensive" |
| `uniqueness` | "very_high" / "high" / "medium" / "low" |
| `popularity_score` | 0-100 composite (reviews + rating + gift suitability + gift proven) |

---

## Recommendation Engine

### Architecture

```
Gift Context (recipient, occasion, budget, interests)
    │
    ├─ SQL Prefilter (SQLite)
    │   ├─ Price range filter
    │   ├─ Occasion matching (JSON LIKE)
    │   ├─ Relationship matching
    │   ├─ Last-minute filter (if < 3 days)
    │   ├─ Rating filter (>= 3.5)
    │   └─ Ordering boosts:
    │       ├─ Interest trait matching
    │       ├─ Review count + rating
    │       ├─ Gift-proven (+3)
    │       ├─ Gift suitability score (+2)
    │       ├─ Matching occasions in gift dimensions (+2)
    │       ├─ Matching relationships in gift dimensions (+2)
    │       └─ Uniqueness for wild card diversity (+1)
    │
    ├─ Diversity enforcement
    │   ├─ Max 2 products per brand
    │   └─ Max 12 per category
    │
    ├─ 50 candidates → LLM Ranking (OpenAI gpt-4o-mini)
    │   ├─ Slot 1: TOP PICK (highest confidence, stated direction)
    │   ├─ Slot 2: GREAT MATCH (different category, sentimental angle)
    │   └─ Slot 3: WILD CARD (surprising, high delight potential)
    │
    ├─ LLM receives per product:
    │   ├─ name, brand, price, category, description
    │   ├─ traits, mood (psychological fit)
    │   ├─ usageSignal
    │   ├─ rating + customerSays (real quotes)
    │   ├─ reviewThemes, giftSignals, qualityCaveat
    │   ├─ giftScore, giftProven, givenTo, givenFor
    │   └─ uniqueness, fitNotes, regiftRisk
    │
    ├─ Post-filter
    │   ├─ Budget compliance (hard ceiling)
    │   ├─ Category diversity (no duplicates)
    │   └─ Brand diversity
    │
    └─ Output per recommendation:
        ├─ whyThisFits (personalized, references recipient by name)
        ├─ giftAngle (how to present/frame the gift)
        ├─ whatThisSays ("This says: 'I notice...'")
        ├─ usageSignal (how often they'll use it)
        ├─ socialProof ("Rated 4.8/5 by 2,340 buyers")
        ├─ qualityCaveat (sizing/durability warnings)
        └─ shopify.variantId (for instant checkout)
```

### Context Accumulation (Learning Loop)

After each session + feedback:
- `lib/context-accumulator.ts` extracts patterns
- Updates user preferences (category, price, style history)
- Updates recipient insights (what works/doesn't per category)
- Feeds back into next recommendation via `buildAccumulatedContext()`

```
Session 1: Gave Sarah a cookware set → loved it
Session 2: Present Agent knows: "Kitchen gifts work for Sarah (100% hit rate)"
           → Boosts kitchen/cooking products, avoids categories that got "meh"
```

---

## Shopify Commerce Integration

### Store Setup

| Property | Value |
|----------|-------|
| Domain | `xrbthg-vv.myshopify.com` |
| Plan | Basic ($39 CAD/mo) |
| Currency | CAD |
| Products synced | ~8,000+ (targeting 100K+, sync running) |
| Metafield definitions | 16 gift intelligence fields |
| Storefront API | Public token for cart/checkout |
| Admin API | Full access (products, orders, files, inventory) |

### Product Sync Strategy

Products are synced in tiers by quality signal:
- **Tier 1:** Gift-proven, 4.5+ rating, 10+ reviews → synced first
- **Tier 2:** 4.0+ rating, 5+ reviews, suitability >= 0.6
- **Tier 3:** Enriched, with images, suitability >= 0.5
- **Tier 4:** All remaining enriched with images

Diversity enforced: max 20 per brand, max 5 per brand+category combination.

Each product carries 16 metafields: review_rating, review_count, gift_suitability, social_proof, usage_signal, what_this_says, quality_notes, uniqueness, fit_notes, review_themes, gift_signals, occasions, relationships, psychological_fit, occasion_fit, source_id.

### Checkout Flow

```
User picks a product (via /gift skill)
    → Storefront API: cartCreate with variant ID
    → Cart attributes: session_id, recipient_name, occasion
    → Cart note: gift message
    → User redirected to Shopify hosted checkout
    → Payment processed by Shopify
    → Webhook fires: orders/create
    → Present Agent links order to gift_session
    → Delivery tracking via fulfillment webhooks
    → 7-day feedback trigger
```

---

## Claude Code Skills (CLI Interface)

### `/gift` — Find a Gift

Conversational gift finder. 2-3 turns max.

```
You: /gift
Agent: Who's the gift for and what's the occasion?
You: My partner Sarah, birthday next month, she's into yoga. $75-100.
Agent: [Calls /api/gift/recommend]

  1. TOP PICK: Heart Padlock Necklace — $75
     5/5 stars from 25 reviews
     "Sarah loves yoga and cooking, and this elegant necklace
      adds sophistication to her daily outfits..."

  2. GREAT MATCH: Brightland Olive Oil Set — $62
     "Rated 4.9/5 by 515 buyers"
     ...

  3. WILD CARD: Daily Driver Kit — $99
     ...

  Like one of these?
```

### `/buy` — Checkout

Creates Shopify cart, opens checkout in browser.

```
You: I'll take #1
Agent: [Creates cart via Storefront API]
       Checkout is open! Heart Padlock Necklace for $75 CAD.
       Complete payment in your browser.
```

### `/remind` — Upcoming Occasions

Scans Google Calendar + Contacts for gift-worthy occasions.

```
You: /remind
Agent: Upcoming occasions:
       Sarah's birthday — June 15 (81 days)
       Mother's Day — May 11 (46 days)
       Want me to find a gift? Run /gift
```

---

## The 9-Phase Gifting Journey

### Implementation Status

| Phase | What | Status | Implementation |
|-------|------|--------|---------------|
| 1. Trigger | Calendar/contact reminders | **Partial** | `/remind` skill, Google Calendar/Contacts API. Missing: proactive notifications, cron automation |
| 2. Person Context | Recipient profiles, auto-memory | **Built** | `recipients` table, `lib/profiles.ts`, context accumulation. Missing: external research |
| 3. Search | Budget/occasion/trait filtering | **Built** | Full prefilter with 10+ boost signals, gift dimensions |
| 4. Idea Maze | Abstract → concrete funnel | **Built** | Claude chat flow, 2-3 turns, direction-picking |
| 5. Compare | Reviews, social proof, caveats | **Built** | 236K reviews, themes, gift signals, quality notes |
| 6. Purchase | Own checkout | **Built** | Shopify Storefront API cart → hosted checkout |
| 7. Card | AI gift message | **Built** | `lib/cards.ts` generates personalized messages |
| 8. Delivery | Tracking, concierge | **Partial** | Webhook handler for fulfillments. Missing: concierge service, courier integration |
| 9. Feedback | Recipient reactions, learning | **Built** | Feedback system, context accumulator, quality scores. Missing: automated 7-day follow-up |

---

## User Experience Design

### User Profile (`/dashboard/profile`)

Shows: recipients with interests, gift history with reactions, learned preferences (categories, budget patterns), data export/delete.

### Settings (`/dashboard/settings`)

AI behavior sliders:
- **Question depth**: minimal ←→ thorough
- **Surprise level**: safe ←→ adventurous
- **Budget strictness**: flexible ←→ strict

Privacy toggles:
- Remember conversations (on/off)
- Learn from outcomes (on/off)
- Suggest from history (on/off)
- Share anonymized data (on/off)

### Data Transparency

Users can see everything Present Agent knows about them and their recipients. Full data export (JSON) and account deletion (GDPR-compliant).

---

## Admin Interface

### Product Admin (`/admin`)
Browse 171K products with filters: category, price tier, store, enrichment status.

### Review Browser (`/admin/reviews`)
Browse 12,652 reviewed products. Features:
- Filter by store, category, min rating
- Sort by most reviewed, highest rated, price
- Live Okendo reviews (fetched on-demand, 10 per product)
- Review intelligence tags: themes (blue), gift signals (purple), quality warnings (orange)
- Star breakdown bars
- Verified buyer badges

---

## Key Technical Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| SQLite over Postgres | Simpler, zero ops, fast for 171K products | Single-server prototype, no concurrent write pressure |
| OpenAI over Anthropic for recs | API key reliability + cost | gpt-4o-mini is fast/cheap. Claude for chat only. |
| Shopify over custom checkout | Trust, payment processing, compliance | Don't build payment infra for a prototype |
| Okendo API over Firecrawl for reviews | Free, structured JSON, unlimited | Firecrawl at 1 credit/page; Okendo is 0 cost |
| Claude Code CLI over web UI | Matches agentic commerce thesis | Users' agents should talk to Present Agent, not users filling forms |
| Headless Shopify over Hydrogen | Keep existing Next.js app | No framework migration needed |
| V3 over V2 architecture | Single LLM call over 11-agent orchestrator | Simpler, faster, production-scale, real data |

---

## Database Schema (key tables)

### `products` (171,450 rows)
Core catalog with 5 enrichment layers. 40+ columns including gift intelligence, reviews, review intelligence, and gift dimensions.

### `shopify_product_map`
Maps SQLite product IDs to Shopify product/variant IDs for checkout.

### `store_quality`
Per-store review platform detection (okendo, yotpo, etc.) and subscriber IDs.

### `users`, `recipients`, `gift_sessions`, `gift_history`
User profiles, recipient profiles with accumulated insights, session tracking, and gift outcome history.

### `conversation_messages`
Full chat transcripts with extracted context per turn.

---

## Scripts Reference

| Script | What | Speed |
|--------|------|-------|
| `crawl-stores.ts` | Crawl 282 Shopify stores | ~1 store/sec |
| `enrich-products.ts` | Gift intelligence via Claude Sonnet (50 workers) | ~5,000/min |
| `scrape-reviews.ts` | Okendo API review scraper | ~200/min (free) |
| `scrape-reviews-firecrawl.ts` | Firecrawl discover + bulk scrape | 1/sec (1 credit each) |
| `enrich-from-reviews.ts` | Review intelligence via OpenAI | ~10/min |
| `enrich-gift-dimensions.ts` | Gift dimensions via OpenAI (15 workers) | ~8/sec |
| `sync-to-shopify.ts` | Product sync to Shopify with metafields + images + auto-publish | ~2/sec |
| `simulate-gift-journey.ts` | LLM-simulated user testing (5 personas) | ~30sec/persona |

---

## Security

- **API keys**: 1Password vault "Agents" (Shopify, OpenAI, Gemini, Firecrawl)
- **Git secret scanning**: Global gitleaks pre-commit + pre-push hooks (`~/.config/git/hooks/`)
- **Shopify webhooks**: HMAC signature verification
- **User data**: GDPR-compliant export + deletion endpoints

---

## Go-Live Checklist

| Step | Status | Owner |
|------|--------|-------|
| Transfer Shopify to paid plan ($39 CAD/mo) | Pending | Guillaume |
| Set up Shopify Payments (bank account + ID) | Pending | Guillaume |
| Disable password page | Pending | Guillaume |
| Configure shipping (flat rate, Canada) | Pending | Guillaume |
| Set GST/HST number | Pending | Guillaume |
| Add policies (privacy, terms, refunds) | Pending | Guillaume |
| Deploy webhook endpoint to Railway | Pending | Dev |
| Sync 100K+ products to Shopify | Running | Automated |
| Refresh API keys in production .env | Pending | Guillaume |

---

## Open Questions

1. How to handle fulfillment at scale? (Manual dropship → wholesale partnerships)
2. Card as standalone product / entry point? (Lower barrier than full gift purchase)
3. Regional courier integration for concierge delivery?
4. How to onboard users who don't use Claude Code? (Web UI vs CLI)
5. Agent-to-agent protocol for agentic commerce? (How do other agents discover Present Agent?)
6. How to make recipient feedback feel safe and not awkward?

---

## Metrics (as of 2026-03-26)

| Metric | Value |
|--------|-------|
| Total products | 171,450 |
| Products with gift intelligence | 171,450 (100%) |
| Products with reviews | 12,652 (236,731 total reviews) |
| Products with review intelligence | 9,686 |
| Products with gift dimensions | 171,020 (99.7%) |
| Products on Shopify | ~8,000+ (syncing to 100K+) |
| Gift-proven products | 9,600 |
| Avg gift suitability score | 0.77 |
| Avg review rating (reviewed products) | 4.92 |
| Unique brands | 623+ on Shopify |
| Simulation pass rate | 4/5 personas (8.3/10 avg) |
| Firecrawl credits used | 500/500 ($0) |
| Total enrichment cost | ~$15 (OpenAI gpt-4o-mini) |
