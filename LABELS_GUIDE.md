# GitHub Labels & Issue States Guide

## 📋 Simple Labeling System

### Rule: ONE workflow label = LAST completed step

Don't stack workflow labels - only show where you are in the process.

---

## 🏷️ Label Categories

### 1. Workflow Labels (ONE at a time)

Shows the **last completed agent step**:

| Label | Applied When | Next Step |
|-------|--------------|-----------|
| `workflow: idea` | @idea completed customer letters | Run @research (PRODUCT) or @spec (TOOL) |
| `workflow: research` | @research completed market validation | Run @spec |
| `workflow: spec` | @spec completed product brief | Run @tech |
| `workflow: tech` | @tech completed technical analysis | Run @launch |
| `workflow: launch` | @launch created implementation repo | Start coding in new repo |

**How to update**: When agent completes, **replace** the workflow label:
```bash
# Example: Moving from spec to tech
gh issue edit <number> --remove-label "workflow: spec" --add-label "workflow: tech"
```

---

### 2. Type Labels (Classification)

Applied by @idea agent:

| Label | Meaning | Workflow |
|-------|---------|----------|
| `type: PRODUCT` | Monetizable product | idea → research → spec → tech → launch |
| `type: TOOL` | Internal/personal use | idea → spec → tech → launch (skip research) |

---

### 3. Status Labels

| Label | When to Use |
|-------|-------------|
| `status: in-progress` | Repo created, coding happening in new repo |

---

## 🔄 Issue Lifecycle

### Phase 1: Planning (Issue = Open)

**State**: Open
**Labels**: One workflow label showing current step
**Activity**: Running agents (@idea → @research → @spec → @tech → @launch)

```
Example at spec stage:
- State: Open
- Labels: type: PRODUCT, workflow: spec
```

---

### Phase 2: Implementation (Issue = Open + in-progress)

**State**: Open
**Labels**: `workflow: launch` + `status: in-progress`
**Activity**: Coding happens in the NEW repository

```
Example:
- State: Open
- Labels: type: TOOL, workflow: launch, status: in-progress
- New repo: https://github.com/user/project-name
```

**Why keep issue open?**
- Track that work is happening
- Document learnings when done
- Compare assumptions vs. reality

---

### Phase 3: Complete & Extract Learnings (Issue = Closed)

**When to close**: User returns with completed project

**Before closing, document**:
1. **What was built** (final scope)
2. **Assumptions tested** (from product.md Section 2)
3. **What worked** (successful validations)
4. **What didn't work** (failed assumptions)
5. **Key learnings** (before vs. after)
6. **Metrics achieved** (vs. goals in product.md)

**Template for final comment**:
```markdown
## 🎓 Project Complete - Learnings

**Repository**: [link]
**Duration**: [X weeks]
**Status**: [Successful MVP / Validated assumptions / Pivot needed / Killed]

### Assumptions Tested (from product.md Section 2)

#### Assumption 1: [Name]
- **Hypothesis**: [What we thought]
- **Test**: [How we tested]
- **Result**: ✅ Validated / ❌ Rejected / 🔄 Partially validated
- **Learning**: [What we learned]

#### Assumption 2: [Name]
- **Hypothesis**: [What we thought]
- **Test**: [How we tested]
- **Result**: ✅ Validated / ❌ Rejected / 🔄 Partially validated
- **Learning**: [What we learned]

### Metrics Achieved

| Metric | Goal (from product.md) | Actual | Status |
|--------|------------------------|--------|--------|
| [Metric 1] | [Target] | [Actual] | ✅/❌ |
| [Metric 2] | [Target] | [Actual] | ✅/❌ |

### Key Learnings

**What worked better than expected**:
- [Learning 1]
- [Learning 2]

**What didn't work as expected**:
- [Learning 1]
- [Learning 2]

**What we'd do differently**:
- [Learning 1]
- [Learning 2]

### Recommendation

- [ ] Ship to production
- [ ] Continue iterating
- [ ] Pivot to [new direction]
- [ ] Kill - not viable

---

*Closing issue now that learnings are documented.*
```

**Then close**:
```bash
gh issue close <number> --comment "Learnings documented above. Project complete."
```

---

## 📊 Common Queries

### View all issues in planning phase
```bash
gh issue list --state open --label "workflow: idea"
gh issue list --state open --label "workflow: spec"
gh issue list --state open --label "workflow: tech"
```

### View all issues in implementation phase
```bash
gh issue list --state open --label "status: in-progress"
```

### View all PRODUCT ideas being validated
```bash
gh issue list --state open --label "type: PRODUCT"
```

### View all TOOL ideas (skip research)
```bash
gh issue list --state open --label "type: TOOL"
```

### View completed projects with learnings
```bash
gh issue list --state closed --label "workflow: launch"
```

---

## 🎯 Label Flow Examples

### Example 1: PRODUCT Idea (Full Workflow)

```
Step 1: @idea runs
├─ State: Open
└─ Labels: type: PRODUCT, workflow: idea

Step 2: @research runs
├─ State: Open
└─ Labels: type: PRODUCT, workflow: research  (removed: workflow: idea)

Step 3: @spec runs
├─ State: Open
└─ Labels: type: PRODUCT, workflow: spec  (removed: workflow: research)

Step 4: @tech runs
├─ State: Open
└─ Labels: type: PRODUCT, workflow: tech  (removed: workflow: spec)

Step 5: @launch creates repo
├─ State: Open
└─ Labels: type: PRODUCT, workflow: launch, status: in-progress

Step 6: User builds in new repo (2-8 weeks)
├─ State: Open (unchanged)
└─ Labels: type: PRODUCT, workflow: launch, status: in-progress

Step 7: User returns, documents learnings
├─ State: Open → Closed
└─ Labels: (unchanged, learnings in final comment)
```

---

### Example 2: TOOL Idea (Skip Research)

```
Step 1: @idea runs
├─ State: Open
└─ Labels: type: TOOL, workflow: idea

Step 2: @spec runs (skip @research)
├─ State: Open
└─ Labels: type: TOOL, workflow: spec

Step 3: @tech runs
├─ State: Open
└─ Labels: type: TOOL, workflow: tech

Step 4: @launch creates repo
├─ State: Open
└─ Labels: type: TOOL, workflow: launch, status: in-progress

Step 5: User builds in new repo
├─ State: Open
└─ Labels: type: TOOL, workflow: launch, status: in-progress

Step 6: User documents learnings & closes
├─ State: Closed
└─ Final comment with before vs. after
```

---

## 🔧 Agent Integration

Each agent should update labels automatically:

### @idea agent
```bash
# After creating issue
gh issue edit <number> --add-label "type: PRODUCT,workflow: idea"
# or
gh issue edit <number> --add-label "type: TOOL,workflow: idea"
```

### @research agent
```bash
# When starting
gh issue edit <number> --remove-label "workflow: idea" --add-label "workflow: research"
```

### @spec agent
```bash
# When starting
gh issue edit <number> --remove-label "workflow: research" --add-label "workflow: spec"
# or (for TOOL, skip research)
gh issue edit <number> --remove-label "workflow: idea" --add-label "workflow: spec"
```

### @tech agent
```bash
# When starting
gh issue edit <number> --remove-label "workflow: spec" --add-label "workflow: tech"
```

### @launch agent
```bash
# When starting
gh issue edit <number> --remove-label "workflow: tech" --add-label "workflow: launch,status: in-progress"
```

---

## 📈 Benefits of This System

1. **Simple**: One workflow label = where you are
2. **Clear**: Open + in-progress = actively building
3. **Learning-focused**: Closing requires documenting insights
4. **Trackable**: Easy to see all projects in each phase
5. **Historical**: Closed issues = knowledge base of what works/doesn't

---

## 🎓 Example: Issue #10 (Tao of Founders)

**Current state**:
- State: Open
- Labels: `type: TOOL`, `workflow: launch`, `status: in-progress`
- New repo: https://github.com/GuillaumeRacine/tao-founders-knowledge-explorer

**What this means**:
- Planning complete (all agents ran)
- Repository created
- Currently building Week 1-8 implementation
- Issue stays open until project completes

**When to close**:
After completing the tool, document:
- Did semantic search hit 80%+ relevance? (Assumption 1)
- Did drafts maintain voice with <50% edit time? (Assumption 2)
- Was it used 12+ of 14 days? (Assumption 3)
- Did it save 30+ min/day? (North Star Metric)
- Key learnings about RAG for personal knowledge bases

Then close with learnings documented.

---

*Last updated: 2025-11-03*
