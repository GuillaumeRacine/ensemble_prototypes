# Research Screening Agent - Product Brief

> Deep research screener + belief system management + decision journal.
> New project -- feeds into all other prototypes.

---

## Vision

An autonomous research agent that continuously screens for insights across multiple domains, manages a structured belief system with explicit assumptions, and maintains a decision journal -- enabling systematic, scientific thinking across all of Guillaume's projects.

---

## Core Capabilities

### 1. Deep Research Screener
- Not alerts or news monitoring (that's DN Monitor)
- **Deep researcher** that can "spill out insights, projections, expectations"
- Screens for trends, patterns, new topics, emerging ideas
- Focus on things that are **counterintuitive but correct**
- Maintain long list of screens, each producing periodic research outputs

### 2. Belief System Management
- Document all assumptions and beliefs explicitly
- **Test beliefs**: how do I form them? How do I counter them?
- Rapidly iterate: find flaws, find where markets/thinking might be wrong
- "Completely revamp your belief system" on demand
- Scientific approach: hypothesis -> test -> update

### 3. Decision Journal
- Record significant decisions with context
- Why I'm doing what I'm doing
- Link decisions to beliefs and research
- Review outcomes against predictions

---

## Research Screens (domains)

| Screen | Focus | Frequency |
|--------|-------|-----------|
| Anti-fragile investment strategies | Systems that improve under stress | Weekly |
| AI tools & products | New coding tools, LLM models, agent frameworks | Daily |
| Hacker News monitor | What people are excited about, new launches | Daily |
| Recommendation systems | All fields -- commerce, content, social | Weekly |
| Multi-agent orchestration | How to use/orchestrate multi-agent systems | Weekly |
| Model capabilities & limitations | What next models can do, current limits, research direction | Weekly |
| ADHD & neurodiversity | Especially in entrepreneurship context | Bi-weekly |
| Neuroscience | General neuroscience advances | Bi-weekly |
| Entrepreneurial psychology | Founder psychology, performance psychology | Weekly |
| Wild card science | Mind-blowing discoveries in biology, engineering, neuro, any field | Weekly |

---

## Belief System Structure

```
Belief:        [statement]
Confidence:    [1-10]
Evidence For:  [supporting data/research]
Evidence Against: [counter-evidence]
Last Tested:   [date]
Test Method:   [how to validate/invalidate]
Status:        [active | revised | invalidated]
```

### Belief Lifecycle
1. **Form**: From research, observation, or intuition
2. **Document**: Explicit statement with confidence level
3. **Test**: Design tests, seek counter-evidence
4. **Update**: Aggressively revise based on evidence
5. **Archive**: Keep history of belief evolution

---

## Integration Points

| Project | How Research Agent Feeds It |
|---------|---------------------------|
| RRSP System | Investment themes, strategy ideas, mispricing signals |
| Present Agent | Recommendation system research, agentic web insights |
| Music Gear | Market trends, e-commerce patterns |
| Tao Publishing | Entrepreneurial psychology research, content ideas |
| Personal growth | ADHD research, neuroscience insights |

---

## Technical Design

- Autonomous execution: runs on schedule, reports findings
- Uses academic research pipeline (6 agents, 5 scripts already exist)
- Extends HN/web monitoring beyond current DN Monitor scope
- Structured output: each screen produces a research brief
- Belief database: queryable, versioned, linked to evidence
- Decision journal: timestamped, linked to beliefs and outcomes

---

## Issues to Create

- [ ] Screen framework: define screen format, scheduling, output structure
- [ ] Belief system database: CRUD + versioning + confidence tracking
- [ ] Decision journal: capture, link to beliefs, review cadence
- [ ] Individual screens (10 domains listed above)
- [ ] Integration with academic research pipeline
- [ ] Auto-counter-argument generator (challenge own beliefs)
- [ ] Periodic belief review: flag stale or untested beliefs
- [ ] Feed research outputs to downstream projects
