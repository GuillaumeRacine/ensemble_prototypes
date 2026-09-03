# Promotion rule — research card → build repo

Status: locked 2026-09-03 (disc-d142335bd807 act).

## What this repo is
`ensemble_prototypes` is the **only** durable home for product/tool ideation and research.
Implementation code is **never** written here.

## Promotion gate (all required)

A card may leave research and start a build **only when**:

1. **Card complete** — every `idea_card` field filled (problem, why-you, alternative, riskiest assumption, 24h-done, kill, budget, evidence).
2. **Type path done**
   - PRODUCT: research evidence logged; go recommendation stands.
   - TOOL: research may be skipped; spec/tech still required if complexity > trivial.
3. **Kill criterion still open** — not already falsified.
4. **WIP slot free** — at most **one** card combined in `ready` + `building` / `status: in-progress`.
5. **Named build target** — either an existing live repo (absorb) or a **new** repo name agreed before first commit.
6. **24h clock** — wall-clock starts at first build commit or explicit `building` label; stop at 24h-done or kill, whichever first.
7. **Gui act** — discuss `act` or explicit in-thread go. Intake alone is not authorization.

## On promote

1. Label card `status: in-progress` (and keep one workflow label).
2. Create or open the **separate** build repo. Link it under Links.
3. No second parallel build card.
4. Same-day backward note on stop: what shipped, what killed, hours/touches/tokens, keep/drop/park.

## Explicit non-promotes

- Stamp/punch commodity clones without a falsifiable gift/P2P (or other) wedge test.
- Town halls, multi-model routers, unified thread UIs, token OS meta — park until one empty skeleton cycle has run.
- Dual intake queues (#discuss **and** ad-hoc GH dumps without a discuss link).
- OPS items — route out within 7 days; do not promote to product repos from here.

## Bridge from Hermes factory

Local learning factory (`~/.hermes/factory/`, `factory_cli.py`) may hold a 24h dogfood card with WIP=1.
Durable research state still lives as a GH issue here. Discuss id goes in Links.
