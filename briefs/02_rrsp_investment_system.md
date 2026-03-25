# RRSP Autonomous Investment System - Product Brief

> Multi-agent system for autonomous RRSP portfolio management.
> Existing repo: `rrsp-investment-system`

---

## Vision

A self-improving multi-agent investment system that autonomously researches, tests, executes, and learns from investment strategies within a Canadian RRSP account, maximizing long-term capital gains through anti-fragile, uncorrelated asset allocation.

---

## Core Investment Principles

### Absolute Requirements
1. **Long-term horizon**: 10-20+ year compounding focus
2. **Low correlation**: Assets/strategies must be fairly uncorrelated with each other
3. **Anti-fragile**: Investments that get stronger under stress/chaos
4. **Asymmetric**: Small downside relative to potential upside
5. **Each investment attractive standalone**: Every position must justify itself independently
6. **RRSP-compliant**: Everything must be available within a Canadian RRSP

### Guidelines (Best-Effort)
- Maximize expected value (odds x payoff)
- Monitor odds continuously for attractiveness
- Systematic and scientific approach to everything
- Explicit documentation of beliefs, assumptions, decisions

---

## System Architecture

### Agent 1: Research & Ideation
- Access historical data, run analysis on demand
- Screen: indices, industries, currencies, individual stocks
- Correlation analysis, regression analysis
- Review academic papers and open-source research
- Surface new ideas and strategies
- Output: ranked list of potential strategies with evidence

### Agent 2: Strategy Testing (Backtester)
- Take strategies from Agent 1
- Run historical backtests
- Score strategies on: returns, risk, correlation, drawdown
- Identify what drives actual returns
- Double down on winners, kill losers

### Agent 3: Portfolio Construction
- Organize strategies into **buckets** (asset type or strategy type)
- Each bucket has its own allocation and optimization target
- Cross-bucket allocation optimization
- Ensure low inter-bucket correlation
- Rebalance recommendations per investment cycle (weekly/monthly)

### Agent 4: Execution
- Autonomous trading via **Interactive Brokers API**
- Execute portfolio decisions without human input
- Handle order types, timing, fees
- Track all trades with full instrumentation

### Agent 5: Review & Self-Improvement
- Review own performance: inputs, outputs, decisions
- Extract learnings across all agents
- Identify what works and what doesn't
- Report back on performance (no human input needed unless steering)
- Fix itself, learn by itself

---

## Strategy Domains

### 1. Surprise/Mispricing Strategy
- Focus on gaps between expectations and reality
- When the gap closes, capture the upside
- Screen for: consensus views vs. reality, under-researched areas
- "Investments are about surprises" -- what's mispriced?

### 2. Options Trading (RRSP-eligible)
- Academic research on options strategies
- Test autonomously, score by strategy type (arbitrage, directional, etc.)
- Systematic, research-driven approach
- Available underlying stocks/options in Canadian RRSP
- Autonomous execution via IB

### 3. International / Emerging Markets
- **India IT sector**: How much AI revenue growth is priced into Indian IT?
- Use AI to process foreign language financial statements (Japanese, etc.)
- Top-down framework: Ruchir Sharma's "10 Rules for Winning Nations" as template
- Stack-rank country/sector attractiveness
- Bottom-up: company strengths vs. current multiples
- Cross-region mispricing arbitrage
- **RRSP constraint**: Likely needs ETFs for international exposure
- Consider ETF fees in analysis

### 4. Cash Flow Growth Investing
- Focus on **cash flow growth**, not just revenue growth
- 10+ year cash flow growth projections at current prices
- Qualitative screening of company strengths
- Pricing/multiples analysis

---

## Data & Instrumentation

| Data Type | Purpose |
|-----------|---------|
| Historical prices | Backtesting, trend analysis |
| Financial statements | Fundamental analysis, cash flow |
| Academic papers | Strategy ideation |
| Correlation matrices | Portfolio construction |
| Trade logs | Self-review, learning |
| Decision journal | Track beliefs, assumptions, outcomes |
| Foreign language docs | AI-translated financial statements |

### Self-Improvement Loop
```
Research -> Hypothesize -> Test -> Execute -> Measure -> Learn -> Research
```
- Instrument everything: every decision, every trade, every outcome
- Autonomous review cycles
- Human can steer but isn't required
- Gradually increase allocation to autonomous agents as trust builds

---

## RRSP Constraints (Canada)

- Stocks (domestic + foreign via ETFs)
- Options (limited -- covered calls, puts on owned stock)
- ETFs (broad access to international markets)
- Bonds / fixed income
- No crypto, no margin, no short selling
- Foreign withholding tax on dividends (15% US, varies by country)
- Consider fee impact on all strategies

---

## Open Questions

1. What's actually RRSP-eligible for options? (covered calls, cash-secured puts confirmed; spreads TBD)
2. Interactive Brokers API access for autonomous trading -- approval process?
3. How to handle the "start small, scale up" trust-building phase?
4. Which academic paper sources to prioritize for strategy ideation?
5. How to structure the decision journal for maximum learning?
6. ETF selection framework for international exposure?

---

## Issues to Create

- [ ] Research agent: academic paper scanner + strategy ideator
- [ ] Backtester agent: historical analysis + strategy scoring
- [ ] Portfolio construction: bucket system + correlation optimization
- [ ] IB API integration: autonomous order execution
- [ ] Self-review agent: performance analysis + learning extraction
- [ ] Options trading sub-system (RRSP-eligible strategies)
- [ ] International investing: country/sector ranking model
- [ ] Cash flow growth screener
- [ ] Surprise/mispricing scanner
- [ ] Decision journal + belief tracking system
- [ ] Instrumentation: full trade + decision logging
- [ ] RRSP eligibility validator
