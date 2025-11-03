# Ensemble Prototypes: Ideation & Research Space

## 🚨 CRITICAL: GitHub Issues Only - Zero Code Implementation

**This repository is EXCLUSIVELY for GitHub issues tracking and research documentation.**

### Absolute Rules for Claude Code:
- ❌ **NEVER write implementation code in this repository**
- ❌ **NEVER create application files** (package.json, requirements.txt, src/, etc.)
- ❌ **NEVER create Docker configs** for applications (Dockerfile, docker-compose.yml)
- ❌ **NEVER create deployment configs** for applications
- ❌ **NEVER install dependencies** for prototype applications here

### What IS Allowed:
- ✅ **CREATE and UPDATE GitHub issues** for prototype tracking
- ✅ **GENERATE research documentation** (markdown files)
- ✅ **RUN web searches** and fetch external documentation
- ✅ **ANALYZE technical landscapes** and create reports
- ✅ **SYNTHESIZE product briefs** from research
- ✅ **CREATE NEW REPOSITORIES** for validated prototypes (code goes THERE)

### Critical Understanding:
**Each prototype gets its own repository. Implementation code lives in those new repositories, NEVER here.**

This is a thinking and planning workspace. Code is forbidden. GitHub issues are the primary artifact.

---

## 🤖 Subagents Workflow Architecture

This repository uses specialized AI agents that operate sequentially to validate prototype ideas through GitHub issues.

### Core Principle: Agents Work on GitHub Issues

**ALL agent work is added to GitHub issues as comments or updates. No code is written in this repository.**

### Available Agents

#### 1. **Idea Agent** (`@idea`)
**Purpose**: Transform raw ideas into customer-centric problem statements
**Input**: One-sentence product/tool idea
**Output**: New GitHub issue with:
- Customer letters (Amazon Working Backwards method)
- Jobs-to-be-done framework
- PRODUCT vs TOOL classification
- Initial problem framing

**Usage**: `@idea "your one-sentence idea"`

---

#### 2. **Research Agent** (`@research`)
**Purpose**: Validate market opportunity and demand
**When**: Only for PRODUCT ideas (skip for TOOLs)
**Input**: GitHub issue URL from idea
**Output**: Comment on issue with:
- Problem validation with data sources
- Pain level assessment (1-10 scale)
- Competitive landscape analysis
- TAM/SAM/SOM market sizing
- Willingness to pay validation
- Go/No-Go recommendation

**Usage**: `@research [issue-url]`

---

#### 3. **Spec Agent** (`@spec`)
**Purpose**: Synthesize research into comprehensive product brief
**When**: After research (PRODUCTS) or idea (TOOLS)
**Input**: GitHub issue URL with prior research
**Output**: Comment on issue with:
- Complete product specification
- Testable assumptions (Desirability/Viability/Feasibility)
- Prototype and learning plan
- Success and kill criteria
- User journey and core interactions

**Usage**: `@spec [issue-url]`

---

#### 4. **Tech Agent** (`@tech`)
**Purpose**: Assess technical complexity and implementation options based on product spec
**When**: After spec completes (for both PRODUCT and TOOL ideas)
**Input**: GitHub issue URL with completed product brief
**Output**: Comment on issue with:
- Complexity score (1-10 with justification)
- Core technical challenges
- 3 implementation options (simple/balanced/robust)
- Build vs buy vs integrate analysis
- Technology stack recommendations
- Technical risks and mitigations

**Usage**: `@tech [issue-url]`

---

#### 5. **Launch Agent** (`@launch`)
**Purpose**: Create NEW repository and set up implementation environment
**When**: After tech completes and go-decision is made
**Input**: GitHub issue URL with completed product brief and technical analysis
**Output**:
- **NEW repository created** (outside this repo!)
- Development environment setup in new repo
- Link to new repo posted as comment on issue
- Implementation begins in the NEW repo

**Critical**: This agent creates a SEPARATE repository for code. NO code is written in the Prototypes repository.

**Usage**: `@launch [issue-url]`

---

## 🎯 Sequential Agent Workflow

### For PRODUCT Ideas:
```
1. @idea → Creates GitHub issue
2. @research → Validates market (added to issue)
3. @spec → Synthesizes brief (added to issue)
4. @tech → Assesses complexity (added to issue)
5. @launch → Creates NEW repo with code
```

### For TOOL Ideas (Personal Use):
```
1. @idea → Creates GitHub issue
2. Skip @research (no market validation needed)
3. @spec → Synthesizes brief (added to issue)
4. @tech → Assesses complexity (added to issue)
5. @launch → Creates NEW repo with code
```

---

## 📋 GitHub Issues as Central Artifact

### Issue Structure
Each prototype idea lives in a GitHub issue with sequential agent comments:

```
Issue Title: [PRODUCT/TOOL] Customer Problem: Job-to-be-Done
│
├── Initial Issue Body (from idea)
│   └── Customer letters and JTBD framework
│
├── Comment 1 (from research, PRODUCTS only)
│   └── Market research and validation
│
├── Comment 2 (from spec)
│   └── Complete product brief
│
├── Comment 3 (from tech)
│   └── Technical assessment
│
└── Comment 4 (from launch)
    └── Link to NEW repository with implementation
```

### Issue Labels
- `customer-letters` - Issue created by idea
- `product` - Requires market validation
- `tool` - Personal use, skip market validation
- `market-validated` - Passed research review
- `tech-assessed` - Technical complexity analyzed
- `spec-complete` - Product brief finalized
- `in-development` - Implementation started in new repo

---

## 🎨 Agent Design Principles

1. **Context Isolation**: Each agent has specialized knowledge and can swap context
2. **Sequential Dependencies**: Each agent builds on previous agent's output
3. **GitHub-Centric**: All work products live in GitHub issues
4. **Stateless Execution**: Agents read from issue, add comment, don't maintain state
5. **Clear Handoffs**: Each agent explicitly signals completion

---

## 🚀 Quick Start Guide

### Starting a New Prototype Idea

1. **Capture the Idea**
   ```bash
   @idea "I want to build a tool that helps developers track API rate limits across multiple services"
   ```
   → Creates GitHub issue with customer problem framing

2. **Validate Market** (if PRODUCT)
   ```bash
   @research https://github.com/user/prototypes/issues/123
   ```
   → Adds market research to issue

3. **Generate Product Brief**
   ```bash
   @spec https://github.com/user/prototypes/issues/123
   ```
   → Adds comprehensive spec to issue

4. **Assess Technical Complexity**
   ```bash
   @tech https://github.com/user/prototypes/issues/123
   ```
   → Adds technical analysis to issue

5. **Launch Implementation** (in new repo!)
   ```bash
   @launch https://github.com/user/prototypes/issues/123
   ```
   → Creates new repository, posts link to issue

6. **Continue Development**
   - Switch to the NEW repository
   - All coding happens there
   - Reference original issue for context

---

## 🗂️ Repository Contents

### This Repository Contains:
```
Prototypes/
├── .claude/
│   └── agents/              # Agent definition files
│       ├── idea.md
│       ├── research.md
│       ├── spec.md
│       ├── tech.md
│       └── launch.md
├── README.md                # User-facing documentation
├── CLAUDE.md                # This file - Claude Code instructions
├── CUSTOM_PROMPTS.md        # Agent documentation and history
└── [research files]         # Historical research artifacts
```

### Implementation Repositories (Created by launch):
```
[prototype-name]/            # NEW REPO - Code lives here!
├── src/
├── tests/
├── docs/
├── package.json / requirements.txt
└── README.md
```

---

## 💡 Best Practices for Claude Code

1. **Never write code here**: Always remind user this is research-only
2. **Use GitHub issues**: All prototype tracking via issues
3. **Sequential agents**: Don't skip agents in the workflow
4. **Link repositories**: When launch creates new repo, link back to original issue
5. **Context preservation**: Each agent reads full issue thread before contributing

---

## 🔍 Example Workflow

**User**: "I want to build a Chrome extension that automatically generates alt text for images using AI"

**Claude**:
```
I'll help you validate this idea using our subagents workflow. Let me start by capturing this as a customer-centric problem statement.

@idea "Chrome extension that automatically generates alt text for images using AI"

This will create a GitHub issue with:
- Customer letters explaining the accessibility problem
- Jobs-to-be-done framework
- Classification (likely PRODUCT if you want to sell it)

Once the issue is created, we'll continue with:
- @research to validate market demand
- @spec to create comprehensive specification
- @tech to assess technical complexity
- @launch to create a NEW repository for implementation

Important: All code will live in a NEW repository, not here.
```

---

*Last Updated: January 2025*
*Architecture: Subagents workflow with GitHub issues as central artifact*