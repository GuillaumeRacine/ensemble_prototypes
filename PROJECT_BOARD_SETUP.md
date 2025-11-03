# GitHub Projects Board Setup

## 🎯 Board View for Prototype Workflow

### Quick Setup Instructions

1. Go to: https://github.com/GuillaumeRacine/ensemble_prototypes/projects

2. Click **"New project"** → Select **"Board"** template

3. Name it: **"Prototype Validation Pipeline"**

---

## 📊 Column Configuration

### Column 1: 💡 Idea
- **Filter**: `is:open label:"workflow: idea"`
- **Description**: Customer letters created, needs validation
- **Automation**: Add issues with `workflow: idea` label

### Column 2: 📊 Research (PRODUCT only)
- **Filter**: `is:open label:"workflow: research"`
- **Description**: Market validation in progress
- **Automation**: Add issues with `workflow: research` label

### Column 3: 📋 Spec
- **Filter**: `is:open label:"workflow: spec"`
- **Description**: Product brief completed
- **Automation**: Add issues with `workflow: spec` label

### Column 4: 🔧 Tech
- **Filter**: `is:open label:"workflow: tech"`
- **Description**: Technical analysis completed
- **Automation**: Add issues with `workflow: tech` label

### Column 5: 🚀 Building (In Progress)
- **Filter**: `is:open label:"status: in-progress"`
- **Description**: Repository created, actively building
- **Automation**: Add issues with `status: in-progress` label

### Column 6: ✅ Complete
- **Filter**: `is:closed label:"workflow: launch"`
- **Description**: Built, tested, learnings documented
- **Automation**: Add closed issues with `workflow: launch` label

---

## 🎨 Alternative: Simple 3-Column Board

For a simpler view:

```
┌─────────────────┬─────────────────┬─────────────────┐
│ 📝 Planning     │ 🚀 Building     │ ✅ Complete     │
│                 │                 │                 │
│ is:open         │ is:open         │ is:closed       │
│ -label:         │ label:          │                 │
│ "in-progress"   │ "in-progress"   │                 │
└─────────────────┴─────────────────┴─────────────────┘
```

### Planning Column
- **Filter**: `is:open -label:"status: in-progress"`
- All open issues without in-progress status
- Shows ideas being validated by agents

### Building Column
- **Filter**: `is:open label:"status: in-progress"`
- Repos created, actively coding

### Complete Column
- **Filter**: `is:closed`
- Finished projects with learnings documented

---

## 🔍 Custom Views You Can Create

### View 1: By Type
- **PRODUCT Ideas**: `is:open label:"type: PRODUCT"`
- **TOOL Ideas**: `is:open label:"type: TOOL"`

### View 2: By Stage
- **Needs Research**: `is:open label:"workflow: idea" label:"type: PRODUCT"`
- **Ready to Build**: `is:open label:"workflow: tech"`
- **Currently Building**: `is:open label:"status: in-progress"`

### View 3: Timeline
- **Recent**: Sort by "Recently updated"
- **Oldest**: Sort by "Oldest" (shows stalled projects)

---

## 📱 How to Use the Board

### Moving Cards

**Manual**: Drag and drop issues between columns

**Automatic** (with automation rules):
1. @idea completes → Card in "Idea" column
2. @research completes → Card moves to "Research"
3. @spec completes → Card moves to "Spec"
4. @tech completes → Card moves to "Tech"
5. @launch completes → Card moves to "Building"
6. User closes issue → Card moves to "Complete"

### Adding Issues

- **From board**: Click "+" in any column
- **From issues**: Label automatically places it in correct column

---

## 🎯 Example Board State

Current issue #10 (Tao of Founders Knowledge Explorer):

```
Planning Columns: (empty for #10)
Building Column:
┌────────────────────────────────────────┐
│ 🚀 Building                            │
├────────────────────────────────────────┤
│ #10 Tao of Founders Knowledge Explorer │
│ 🏷️ type: TOOL                          │
│ 🏷️ workflow: launch                    │
│ 🏷️ status: in-progress                 │
│                                        │
│ Week 3 of 8 - Building MVP             │
└────────────────────────────────────────┘
```

After completion and closing:
```
Complete Column:
┌────────────────────────────────────────┐
│ ✅ Complete                             │
├────────────────────────────────────────┤
│ #10 Tao of Founders Knowledge Explorer │
│ 🏷️ type: TOOL                          │
│ 🏷️ workflow: launch                    │
│                                        │
│ ✅ Semantic search: 85% relevance       │
│ ✅ Voice maintained: 40% edit time      │
│ ✅ Daily usage: 13/14 days              │
│ ✅ Time saved: 45 min/day               │
└────────────────────────────────────────┘
```

---

## 🔗 Quick Links

After setup, your board will be at:
`https://github.com/users/GuillaumeRacine/projects/[NUMBER]`

Or repository-level:
`https://github.com/GuillaumeRacine/ensemble_prototypes/projects/[NUMBER]`

---

## 💡 Pro Tips

1. **Pin important projects**: Pin the board to see it on repo homepage

2. **Use milestones**: Group related prototypes (Q1 2025, AI tools, etc.)

3. **Add custom fields**:
   - Priority (High/Medium/Low)
   - Est. Effort (1-8 weeks)
   - ROI Score (1-10)
   - Status emoji (🟢 🟡 🔴)

4. **Mobile app**: GitHub mobile app supports project boards

5. **Share links**: Share filtered views with team/stakeholders

---

## 🎨 Visual Reference

Your workflow visualized:

```
User: @idea "concept"
         ↓
    [💡 Idea]
         ↓
   @research (if PRODUCT)
         ↓
   [📊 Research]
         ↓
      @spec
         ↓
    [📋 Spec]
         ↓
      @tech
         ↓
    [🔧 Tech]
         ↓
     @launch
         ↓
  [🚀 Building] ← Issue stays here (Open + in-progress)
         ↓
   User builds (2-8 weeks)
         ↓
   Documents learnings
         ↓
   [✅ Complete] ← Issue closed
```

---

## 📝 Next Steps

1. Go to: https://github.com/GuillaumeRacine/ensemble_prototypes/projects
2. Click "New project"
3. Choose "Board" template
4. Set up columns using filters above
5. Enable automation for label-based movement
6. Start tracking your prototypes visually!

---

*Alternative: Use GitHub's built-in "Table" view for a spreadsheet-like interface with sortable columns.*
