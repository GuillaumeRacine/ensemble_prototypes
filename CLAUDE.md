# Ensemble Prototypes: Ideation & Research Space

## 🚨 IMPORTANT: No Code Implementation

**This repository is for ideation and research ONLY.** 
- ❌ **DO NOT** write any implementation code here
- ❌ **DO NOT** create technical files (Python, JavaScript, Docker, etc.)
- ✅ **DO** conduct research and create documentation
- ✅ **DO** use GitHub issues to track prototype ideas
- ✅ **DO** generate product briefs and specifications

**Why?** Each prototype will be built in its own standalone repository after proper research and validation. This space is purely for gathering insights and prioritizing opportunities.

---

## 📂 Repository Structure

This repository organizes prototype ideas and research:

### Active Prototype Research
Each prototype idea gets:
1. **GitHub Issue** - For tracking the idea and discussion
2. **Product Brief** - Generated using `/spec` command
3. **Technical Research** - Generated using `/tech_research` command
4. **Assumption Validation Framework** - Key hypotheses to test

### Example: Present Agent (Issue #3)
The Present Agent prototype demonstrates our research process:
- **`present_agent_product_brief.md`** - Complete business model and strategy
- **`mvp_assumption_validation.md`** - Framework for testing assumptions
- **`technical_reference_guide.md`** - Deep technical research
- **`product_guide.md`** - Implementation guidance (for future standalone repo)

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

## 🎯 Workflow for New Prototypes

### Step 1: Create GitHub Issue
```bash
gh issue create --title "[Prototype] Your Idea Name" --body "Brief description"
```

### Step 2: Research & Document
1. Run `/tech_research [your idea]` to understand technical landscape
2. Run `/spec [your idea]` to create comprehensive product brief
3. Create assumption validation framework
4. Document key insights in the issue

### Step 3: Prioritization
- Review all prototype ideas in GitHub issues
- Evaluate based on:
  - Market opportunity size
  - Technical feasibility
  - Resource requirements
  - Assumption testability
  - Strategic fit

### Step 4: Implementation (Separate Repo)
Once a prototype is selected:
1. Create new standalone repository
2. Copy relevant research documents
3. Begin implementation with clear assumptions to test
4. Track progress back to original issue

---

## 💡 Best Practices

1. **Research First** - Thorough research prevents wasted implementation effort
2. **Test Assumptions** - Every prototype must have clear pass/fail criteria
3. **Document Everything** - Future you will thank current you
4. **Use GitHub Issues** - Central tracking for all ideas and discussions
5. **Keep It Clean** - This repo is for thinking, not coding

---

*Last Updated: December 2024*  
*Next Milestone: MVP assumption validation complete*