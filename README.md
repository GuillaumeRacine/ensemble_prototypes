# Ensemble Prototypes

A structured ideation and research space for validating prototype concepts before implementation.

## 🚨 Important: Research Only Repository

**This repository is for ideation and research ONLY.** No implementation code should be added here. Each validated prototype will be built in its own standalone repository.

## Purpose

Ensemble Prototypes provides a systematic approach to:
- 🔍 Research and validate product ideas
- 📋 Generate comprehensive product specifications
- 🧪 Define testable assumptions with clear pass/fail criteria
- 📊 Prioritize opportunities based on data
- 📚 Document insights for future reference

## Custom Claude Code Commands

### `/spec [product idea]`
Generates comprehensive product specifications including:
- Business model canvas
- Risk analysis and assumption validation
- 8-week implementation roadmap
- Success metrics and kill criteria

### `/tech_research [concept]`
Conducts deep technical research covering:
- Technical landscape analysis
- Best practices and proven solutions
- Tool and framework recommendations
- Scalability and performance considerations

### `/improve_spec_prompt`
Optimizes product specification prompts for better clarity and structure

## Workflow

1. **Ideation**: Create a GitHub issue for your prototype idea
2. **Research**: Use `/tech_research` to understand the technical landscape
3. **Specification**: Use `/spec` to create a comprehensive product brief
4. **Validation**: Define clear assumptions with measurable pass/fail criteria
5. **Prioritization**: Review all ideas and select based on opportunity/feasibility
6. **Implementation**: Create a separate repository for the chosen prototype

## Example Prototypes

See our GitHub issues for prototype ideas in various stages:
- Issue #1: Template for new prototype ideas
- Issue #2: AI Sprint Retrospective Tool
- Issue #3: Present Agent (Gift Recommendation Platform)

## Repository Structure

```
ensemble_prototypes/
├── .claude/                      # Custom Claude Code commands
├── CLAUDE.md                     # Guidelines for Claude Code
├── README.md                     # This file
└── [prototype]_[document].md     # Research and specification documents
```

## Contributing

To propose a new prototype:
1. Create a GitHub issue with your idea
2. Use the custom commands to generate research and specifications
3. Add assumption validation framework
4. Document all insights in the issue thread

Remember: **No code in this repository** - only research, documentation, and planning.