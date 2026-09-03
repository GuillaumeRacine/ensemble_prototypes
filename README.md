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

## 2026-09-02 triage baseline (still open work)

24 open → target ≤3 non-parked + parked/absorbed rest. Not executed in the schema/promotion ship.

- Absorbed candidates (live repo owns it): #15 Present, #54 Tao Book, #40 Substack Growth, #51 Ian/Investment, #55 Music Gear, #31 Shopify API ops
- Merge candidates: #36+#37 (POD), #45+#46 (Stoic OS), #52 media, #39 research-screening spine
- Park candidates: #41, #42, #43, #44, #47, #48, #49, #50, #53, #24, #13, #38
- Keep ≤3: research spine, Present absorbed-track, one open slot

Say `act triage` in the discuss thread when you want that sweep run.
