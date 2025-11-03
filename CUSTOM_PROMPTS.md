# Subagents Workflow Documentation

This document provides comprehensive documentation of the subagents workflow used in the Ensemble Prototypes repository.

---

## 📋 Overview

The Ensemble Prototypes workflow uses **specialized AI agents** that work sequentially to validate product ideas through GitHub issues. Each agent has a specific role and produces structured output as comments on GitHub issues.

### Core Principle

**ALL work happens in GitHub issues. NO code is written in this repository.**

Each validated prototype gets its own separate repository for implementation.

---

## 🤖 The Five Agents

### 1. Idea Agent (`@idea`)
### 2. Research Agent (`@research`)
### 3. Spec Agent (`@spec`)
### 4. Tech Agent (`@tech`)
### 5. Launch Agent (`@launch`)

---

## 📊 Agent 1: Idea Agent

**File**: `.claude/agents/idea.md`

### Purpose
Transform raw ideas into customer-centric problem statements using Amazon's "Working Backwards" customer letter approach.

### Input
- One-sentence product or tool idea from user

### Process
1. **Classify**: PRODUCT (monetizable) or TOOL (personal use)
2. **Generate Customer Letters**: 3-4 first-person narratives covering:
   - Current struggle and pain points
   - Job-to-be-done
   - Solution vision
   - Willingness to change/pay
3. **Synthesize JTBD**: Extract core job from customer perspective
4. **Create GitHub Issue**: With all customer letters and classification

### Output
- NEW GitHub issue with:
  - Classification (PRODUCT/TOOL)
  - Customer letters (500-1000 words)
  - Synthesized JTBD
  - Next steps based on classification

### Next Agent
- **PRODUCT** → `@research`
- **TOOL** → `@spec` (skip research)

---

## 📈 Agent 2: Research Agent

**File**: `.claude/agents/research.md`

### Purpose
Validate market opportunity through evidence-based research.

### When to Use
- **ONLY for PRODUCT ideas** (skip for TOOLs)

### Input
- GitHub issue URL from idea

### Process
1. **Problem Discovery**: Search for user complaints, forum discussions, industry reports
2. **Pain Validation**: Quantify time wasted, money lost, frequency, emotional impact
3. **Competitive Landscape**: Map direct competitors, pricing, market gaps
4. **Willingness to Pay**: Assess current spend, budget allocation, ROI expectations

### Research Tools
- WebSearch for market data
- WebFetch for competitor analysis
- Real sources and citations required

### Output
- Comment on GitHub issue with:
  - Pain score (1-10 with justification)
  - TAM/SAM/SOM analysis
  - Competitive analysis table
  - Pricing benchmarks
  - Go/No-Go/Pivot recommendation
  - Make-or-break assumptions

### Key Sections
```
📊 Problem Validation
  - Pain Score: X/10
  - Supporting Data with sources

🎯 Market Opportunity
  - TAM/SAM/SOM
  - Customer segments table

🏁 Competitive Analysis
  - Direct competitors table
  - Indirect solutions
  - Our opportunity

💰 Monetization Validation
  - Pricing benchmarks
  - Revenue model options

✅ Go/No-Go Recommendation
  - Go signals, warning signs, kill signals
  - Overall verdict with rationale
```

### Next Agent
→ `@spec`

---

## 📋 Agent 3: Spec Agent

**File**: `.claude/agents/spec.md`

### Purpose
Synthesize all research into comprehensive, assumption-focused product brief.

### When to Use
- After research (for PRODUCTs) or after idea (for TOOLs)

### Input
- GitHub issue URL with prior research

### Process
1. **Read All Context**: Synthesize idea, research (if PRODUCT) outputs
2. **Risk Analysis Research**: Research comparable products, common failure modes
3. **Create Product Brief**: Comprehensive spec with testable assumptions

### Research Tools
- Read prior agent comments
- WebSearch for validation strategies
- WebFetch for case studies

### Output
- Comment on GitHub issue with:
  - Complete product specification
  - Testable assumptions (Desirability/Viability/Feasibility)
  - Prototype and learning plan
  - Clear success and kill criteria
  - User journey and core interactions

### Key Sections
```
📋 Product Brief
  1. Problem (with evidence from research)
  2. Solution (differentiation from competitive analysis)
  3. Target Audience (ICP from market research)
  4. User Experience (primary journey)
  5. Technical Implementation (high-level overview)
  6. Limitations & Trade-offs
  7. Risks & Testable Assumptions
     - 7.1 Desirability (assumptions with tests)
     - 7.2 Viability (assumptions with tests)
     - 7.3 Feasibility (assumptions with tests)
  8. Prototype & Learning Plan
     - Testing approach and metrics
     - Success criteria
     - Kill criteria
  9. PMF Success Metrics
```

### Next Agent
→ `@tech`

---

## 🔧 Agent 4: Tech Agent

**File**: `.claude/agents/tech.md`

### Purpose
Assess technical complexity and provide implementation options based on the product spec.

### When to Use
- After spec completes (for both PRODUCTs and TOOLs)

### Input
- GitHub issue URL with completed product brief from spec agent

### Process
1. **Technical Landscape Research**: Production implementations, common approaches, benchmarks
2. **Complexity Assessment**: Core challenges, dependencies, required expertise, time estimates
3. **Options & Tradeoffs**: 3 implementation approaches (simple/balanced/robust)

### Research Tools
- WebSearch for technical patterns
- WebFetch for architecture examples
- Real-world implementations required

### Output
- Comment on GitHub issue with:
  - Complexity score (1-10 with justification)
  - 3 implementation options with pros/cons
  - Build vs buy vs integrate analysis
  - Technology stack recommendations
  - Technical risks and mitigations
  - Technical go/no-go verdict

### Key Sections
```
🎯 Complexity Assessment
  - Overall score: X/10
  - Core technical challenges
  - Required expertise
  - Time estimates (MVP/Beta/Production)

🔧 Implementation Options
  - Option 1: Simplest (stack, pros/cons, complexity, timeline)
  - Option 2: Balanced (stack, pros/cons, complexity, timeline)
  - Option 3: Robust (stack, pros/cons, complexity, timeline)

⚖️ Key Tradeoffs
  - Build vs buy vs integrate table
  - Performance vs simplicity
  - Cost vs quality

🚨 Technical Risks
  - High risk items with mitigation
  - Medium risk items
  - Dependencies and lock-ins

✅ Technical Go/No-Go
  - Verdict and reasoning
  - Recommended path forward
```

### Next Agent
→ `@launch` (if GO decision)

---

## 🚀 Agent 5: Launch Agent

**File**: `.claude/agents/launch.md`

### Purpose
Create NEW repository and set up development environment.

### 🚨 CRITICAL
**This agent creates a SEPARATE repository. ALL code goes in the NEW repo, NEVER in Prototypes.**

### When to Use
- After tech completes AND go-decision is made

### Input
- GitHub issue URL with completed product brief

### Process
1. **Read Product Brief**: Extract name, stack, MVP scope, success metrics
2. **Create NEW Repository**: Use gh CLI to create separate repo
3. **Initialize Project** (IN NEW REPO): Set up based on stack recommendation
4. **Create Initial Files** (IN NEW REPO): README, docs, basic structure
5. **Update Original Issue**: Add comment with link to new repo

### Tools Used
- Bash (gh CLI for repo creation)
- Write (IN NEW REPO ONLY)
- Git commands (IN NEW REPO)

### Output
- NEW GitHub repository (outside Prototypes!)
- Comment on original Prototypes issue with:
  - Link to new repository
  - Setup instructions
  - Week 1 MVP scope
  - Implementation checklist

### Key Principles
```
✅ DO: Create new repository
✅ DO: Initialize project IN NEW REPO
✅ DO: Link back to original issue
✅ DO: Provide clear setup instructions

❌ DON'T: Write code in Prototypes repo
❌ DON'T: Create package.json in Prototypes repo
❌ DON'T: Create src/ in Prototypes repo
❌ DON'T: Install dependencies in Prototypes repo
```

### Result
- Separate repository ready for development
- Original issue remains documentation-only
- Clear handoff with context preserved

---

## 🔄 Complete Workflow

### For PRODUCT Ideas

```
User: "I want to build X"
  ↓
@idea
  ↓
[GitHub Issue Created with Customer Letters]
  ↓
@research [issue-url]
  ↓
[Market Research Added as Comment]
  ↓
@spec [issue-url]
  ↓
[Product Brief Added as Comment]
  ↓
@tech [issue-url]
  ↓
[Technical Analysis Added as Comment]
  ↓
@launch [issue-url]
  ↓
[NEW Repository Created]
[Link Posted to Original Issue]
  ↓
Development continues in NEW REPO
```

### For TOOL Ideas

```
User: "I want to build X"
  ↓
@idea
  ↓
[GitHub Issue Created with Customer Letters]
  ↓
Skip @research (no market validation needed)
  ↓
@spec [issue-url]
  ↓
[Product Brief Added as Comment]
  ↓
@tech [issue-url]
  ↓
[Technical Analysis Added as Comment]
  ↓
@launch [issue-url]
  ↓
[NEW Repository Created]
[Link Posted to Original Issue]
  ↓
Development continues in NEW REPO
```

---

## 📂 Repository Structure

### Prototypes Repository (THIS REPO)
```
Prototypes/
├── .claude/
│   └── agents/
│       ├── idea.md              # Agent definitions
│       ├── research.md
│       ├── spec.md
│       ├── tech.md
│       └── launch.md
├── README.md                     # User documentation
├── CLAUDE.md                     # Claude Code instructions
├── CUSTOM_PROMPTS.md             # This file
└── [research files]              # Historical research only

GitHub Issues:
  └── Each issue = one prototype idea
      ├── Issue body (from idea)
      ├── Comment 1 (from research, if PRODUCT)
      ├── Comment 2 (from spec)
      ├── Comment 3 (from tech)
      └── Comment 4 (from launch) → links to NEW repo
```

### Implementation Repositories (CREATED BY launch)
```
[prototype-name]/                 # NEW REPO - Code lives here!
├── src/                          # Application code
├── tests/                        # Test suites
├── docs/
│   ├── product-brief.md         # Copy from spec
│   └── assumptions.md            # Validation tracking
├── package.json                  # Dependencies (or requirements.txt)
└── README.md                     # Setup instructions
```

---

## 🎯 Design Principles

### 1. Context Isolation
Each agent has specialized knowledge and can swap context efficiently.

### 2. Sequential Dependencies
Each agent builds on the previous agent's output.

### 3. GitHub-Centric
All work products live in GitHub issues, not in files.

### 4. Stateless Execution
Agents read from issue, add comment, don't maintain state between invocations.

### 5. Clear Handoffs
Each agent explicitly signals completion and tells user what's next.

### 6. Separation of Concerns
Research (Prototypes repo) is completely separate from code (implementation repos).

---

## 💡 Best Practices

### For Users

1. **Start with idea**: Always begin workflow here
2. **Follow the sequence**: Don't skip agents (except research for TOOLs)
3. **Read agent outputs**: Each provides valuable context for next step
4. **Make explicit decisions**: Agents recommend, you decide GO/NO-GO
5. **Switch repos for coding**: When launch creates new repo, work there

### For Claude Code

1. **Never mix concerns**: Research in Prototypes, code in new repos
2. **Always read context**: Before adding comment, read full issue thread
3. **Be evidence-based**: All claims must have sources
4. **Be brutally honest**: Don't sugarcoat risks or complexity
5. **Clear next steps**: Always tell user exactly what to do next

---

## 🔍 Example Usage

### User starts with idea
```
User: "I want to build a Chrome extension that summarizes long articles using AI"

Claude: I'll help you validate this idea using our subagents workflow.

[Invokes @idea]

✅ GitHub Issue Created: https://github.com/user/prototypes/issues/47

📊 Classification: PRODUCT
This has clear monetization potential - users would pay for time-saving AI summarization.

🎯 Core JTBD:
"Help me quickly understand long articles so I can stay informed without spending hours reading."

📍 Next Steps:
This is a PRODUCT idea, so follow this sequence:
1. @research https://github.com/user/prototypes/issues/47
2. @spec https://github.com/user/prototypes/issues/47
3. @tech https://github.com/user/prototypes/issues/47
4. @launch https://github.com/user/prototypes/issues/47 (if GO)

All work documented in the GitHub issue. No code in this repository.
```

---

## 📚 Version History

### v2.0 (January 2025) - Subagents Workflow
- **Complete rewrite** from custom commands to subagents
- **5 specialized agents** with clear roles
- **GitHub-centric**: All work in issues, no code in this repo
- **Explicit separation**: Research here, code in new repos
- **Sequential workflow**: Clear agent dependencies
- **Context swapping**: Each agent can load fresh context

### v1.0 (December 2024) - Custom Commands
- Initial implementation with `/idea`, `/product`, `/tech`, `/spec`, `/go` commands
- Single-context execution
- Mixed concerns (some code generation in this repo)

---

## 🎓 Key Learnings

### Why Subagents?

1. **Better context management**: Each agent loads only what it needs
2. **Clearer separation**: Research vs implementation are truly separate
3. **Easier to maintain**: Each agent is self-contained
4. **Scalable**: Easy to add new specialized agents
5. **Enforceable boundaries**: Harder to accidentally write code in wrong place

### Migration Notes

If you have existing issues from v1.0 workflow:
- They remain valid as research documentation
- Can invoke v2.0 agents on them to complete analysis
- Clearly mark which workflow version was used

---

**Remember**: This is a thinking space, not a coding space. Ideas mature here through structured research, implementations happen in their own repositories.
