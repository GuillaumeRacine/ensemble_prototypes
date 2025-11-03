# Ensemble Prototypes

A structured ideation and research space for validating prototype concepts before implementation.

---

## 🚨 CRITICAL: GitHub Issues Only - Zero Code Policy

### What This Repository IS:
✅ **GitHub Issues Board** for tracking prototype ideas
✅ **Research documentation** and market analysis
✅ **Product specifications** and technical assessments
✅ **Assumption frameworks** and validation plans

### What This Repository IS NOT:
❌ **NO implementation code** (Python, JavaScript, etc.)
❌ **NO application files** (package.json, requirements.txt for apps)
❌ **NO deployment configs** (Dockerfile, docker-compose.yml for apps)
❌ **NO application dependencies** or build systems

### Where Code Lives:
🎯 **Each validated prototype gets its own separate repository**
🎯 **Implementation happens ONLY in those new repos**
🎯 **This repo remains pure research and planning**

---

## 🤖 Subagents Workflow

This repository uses specialized AI agents that work sequentially to validate ideas:

### Agent 1: Idea Capture → `@idea`
- Transforms ideas into customer-centric problem statements
- Creates GitHub issue with customer letters (Amazon Working Backwards method)
- Classifies as PRODUCT (needs market validation) or TOOL (personal use)

### Agent 2: Market Research → `@research`
- **Only runs for PRODUCT ideas** (skipped for TOOLs)
- Validates market opportunity and willingness to pay
- Adds research findings to the GitHub issue

### Agent 3: Product Brief → `@spec`
- Synthesizes all research into comprehensive product brief
- Defines testable assumptions and success criteria
- Adds final specification to the GitHub issue

### Agent 4: Technical Analysis → `@tech`
- Assesses technical complexity and implementation options
- Evaluates build vs buy vs integrate tradeoffs
- Adds technical assessment to the GitHub issue

### Agent 5: Implementation Launch → `@launch`
- **Creates NEW repository** for the prototype
- Sets up development environment in the NEW repo
- **Code lives ONLY in the new repo, NOT here**

---

## 🎯 How to Use This Repository

### Step 1: Start with an Idea
```bash
# In this repository, invoke the idea agent
@idea "your one-sentence product/tool idea"
```

**Output**: New GitHub issue with customer problem framing

### Step 2: Validate the Market (PRODUCTS only)
```bash
# On the GitHub issue created in Step 1
@research [issue-url]
```

**Output**: Market research added as comment to the issue
**Skip this step for personal TOOLS**

### Step 3: Create Product Brief
```bash
# On the same GitHub issue
@spec [issue-url]
```

**Output**: Comprehensive product specification added to the issue

### Step 4: Assess Technical Feasibility
```bash
# On the same GitHub issue
@tech [issue-url]
```

**Output**: Technical analysis added as comment to the issue

### Step 5: Launch Implementation (separate repo!)
```bash
# On the same GitHub issue with completed analysis
@launch [issue-url]
```

**Output**: NEW repository created with prototype code
**This repo remains code-free!**

---

## 📋 What Lives in GitHub Issues

Each prototype idea is tracked as a GitHub issue containing:

1. **Customer Letters** (from idea)
   - First-person problem narratives
   - Jobs-to-be-done statements
   - Current pain points and alternatives

2. **Market Research** (from research, PRODUCTS only)
   - Problem validation with data sources
   - Competitive landscape analysis
   - TAM/SAM/SOM sizing
   - Monetization validation

3. **Product Brief** (from spec)
   - Complete product specification
   - Testable assumptions framework
   - Prototype and learning plan
   - Clear success metrics

4. **Technical Assessment** (from tech)
   - Complexity scoring and justification
   - Implementation options with tradeoffs
   - Technology stack recommendations
   - Risk analysis and mitigation

5. **Link to Implementation** (from launch)
   - Repository URL for the prototype
   - Setup instructions
   - Initial development status

---

## 🗂️ Repository Structure

```
Prototypes/                           # THIS REPO (no code!)
├── .claude/
│   └── agents/                       # Agent definitions
│       ├── idea.md                  # Customer letters generator
│       ├── research.md              # Market researcher
│       ├── spec.md                  # Product brief synthesizer
│       ├── tech.md                  # Technical analyst
│       └── launch.md                # Implementation launcher
├── README.md                         # This file
├── CLAUDE.md                         # Claude Code instructions
└── CUSTOM_PROMPTS.md                 # Agent documentation

[prototype-name]/                     # NEW REPO (has code!)
├── src/                              # Application code
├── tests/                            # Test suites
├── package.json / requirements.txt   # Dependencies
└── README.md                         # Setup instructions
```

---

## 🎨 Design Philosophy

1. **Separate concerns**: Research here, code elsewhere
2. **GitHub issues as source of truth**: All decisions documented
3. **Agent specialization**: Each agent has one clear job
4. **Context isolation**: Agents can swap context efficiently
5. **Evidence-based decisions**: Real data, not assumptions
6. **Clear handoffs**: Each agent builds on previous work

---

## 🔍 Example Prototypes

Browse our GitHub issues to see prototypes in various stages:
- **Issue #1**: Template for new prototype ideas
- **Issue #2**: AI Sprint Retrospective Tool
- **Issue #3**: Present Agent (Gift Recommendation Platform)

Each issue shows the complete journey from idea to implementation link.

---

## ⚡ Quick Start

```bash
# 1. Have an idea? Start here:
@idea "I want to build X to solve Y for Z users"

# 2. Follow the agents sequentially on the created GitHub issue

# 3. When ready, launch implementation in a NEW repo:
@launch [issue-url]

# 4. Continue development in the NEW repository
# 5. This repo stays clean - just issues and docs!
```

---

## 🚫 Enforcement: What NOT to Do

**DO NOT** add these to this repository:
- Source code files (`.py`, `.js`, `.ts`, `.go`, etc.)
- Package managers (`package.json`, `requirements.txt`, `go.mod`)
- Build configs (`webpack.config.js`, `vite.config.ts`)
- Docker files (`Dockerfile`, `docker-compose.yml`) for applications
- Environment files (`.env`, `.env.example`) for applications
- Node modules, virtual environments, or build artifacts

**Exception**: Research tools that support the workflow itself (like `solana_clm_monitor.py` for research purposes) are OK as they don't represent prototype implementations.

---

**Remember**: This is a thinking space, not a coding space. Ideas mature here, implementations happen elsewhere.