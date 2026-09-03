# Ensemble Prototypes — Source of Truth for Product Ideation & Research

Status: **active operating repo** (revived 2026-09-02; card schema + promotion rule shipped 2026-09-03).

Single durable home for every product/tool idea: capture, research, validation, spec — before any code.

**Decision (Gui):** This repo is the SoT for ALL product ideation and research work. Slack `#discuss` is the front door for intake; approved ideas land here as cards. Implementation lives ONLY in separate repos created at launch/promote.

Tracking discuss item: `disc-d142335bd807`.

---

## Scope contract

- Idea intake + approval gate → Slack `#discuss` (discuss-intake workflow)
- Durable idea cards, research, validation, specs → **this repo** (GitHub issues)
- Implementation code → separate repo per prototype (created at promote/launch)
- Parked ideas archive → this repo, `parked` label + revisit date
- Personal ops (non-prototype) → hermes kanban `admin` — NOT here

One GitHub issue = one idea card. **Zero implementation code in this repo.**

---

## Card lifecycle

```
raw → research → validate → spec → tech → ready → building → learned
                                   ↘ parked (dated)   ↘ absorbed (live repo owns it)
```

- **WIP=1**: at most ONE card in `ready`+`building` combined.
- **≤3 non-parked bets** at any time. Everything else is parked or absorbed.
- PRODUCT cards need research evidence before spec. TOOL cards skip market research.
- OPS items route out within 7 days.
- 30 days with no new evidence → `parked` with revisit date.
- `absorbed`: live repo owns the work; card stays as pointer only.

Full promote gate: [`PROMOTION.md`](./PROMOTION.md).

## Required card fields

Use the **Idea Card** issue template (`.github/ISSUE_TEMPLATE/idea_card.md`):

one-liner, type (PRODUCT/TOOL/OPS), problem, why-you, current alternative, riskiest assumption, 24h-done definition, kill criterion, token/time budget, evidence log, links.

A card cannot leave `raw` until all fields are filled.

## Labels

- Workflow (one at a time): `workflow: idea|research|spec|tech|launch`
- Type: `type: PRODUCT` / `type: TOOL` / `type: OPS`
- Disposition: `parked`, `absorbed`, `status: in-progress`

## Board

Project #4 `ensemble_prototypes` (GitHub Projects v2): Raw → Research → Validate → Spec/Tech → Ready → Building → Learned → Parked.

## Intake bridge

`#discuss` → Hermes discuss-intake packet → Gui picks `act` → agent opens a card here from the Idea Card template → labels `workflow: idea` + type. Discuss thread URL goes in Links.

Local 24h learning factory (optional dogfood): `~/.hermes/factory/` + `factory_cli.py`. Does not replace this SoT.

## Triage status (executed 2026-09-03)

Source: disc-d142335bd807 `act triage`. **24 open → 1 open non-parked.**

- **KEEP (open):** #39 Belief-Testing Workflow (`workflow: idea`, `type: TOOL`) — research spine; build WIP empty.
- **ABSORBED (closed + `absorbed`):** #15 Present, #31 Shopify API ops, #40 Substack Growth, #46 Stoic monthly, #51 Ian/Investment, #52 Media pipeline, #54 Tao Book, #55 Music Gear.
- **MERGED then closed:** #37 → #36 (POD), #45 → #46 (Stoic/company updates).
- **PARKED (closed + `parked`, revisit 2026-12-03):** #13, #24, #36, #38, #41, #42, #43, #44, #47, #48, #49, #50, #53.
- **Empty ≤3 slots:** 2 free (Present lives in present repos as absorbed-track; next idea enters via #discuss → act).

Proof: `~/.hermes/docs/ENSEMBLE_PROTOTYPES_TRIAGE_ACT_PROOF_2026-09-03.md`
