# Agentic Governance Profile Builder

**Live:** [workspace.aistreamlinehub.com](https://workspace.aistreamlinehub.com)

Generate a regulator-defensible governance profile for one AI agent — in under fifteen minutes.

## What it does

Five EU AI Act primitives, applied to a single agent:

| Primitive | What it produces |
|---|---|
| M — Maturity Check | Structural gap score across five governance dimensions |
| P-01 — Decision Boundary Contract | Allowed, prohibited, and conditional action lists |
| P-02 — Oversight Trigger Matrix | Per-action oversight level and entry conditions |
| P-03 — Accountability Canvas | Four-owner mapping with gap diagnostic |
| P-04 — Audit Schema | Handoff receipt template and retention guidance |

**Output:** Governance Profile (PDF) + Gap Register (CSV)

## Modes

- **Pre-deployment** — design governance before the agent goes live
- **In-flight** — refine governance during active build
- **Retrofit** — map what's actually enforced in production today

## Stack

Single-file React app (`public/index.html`) — no build step, no dependencies to install. Deployed on Vercel.

## Repo structure

```
public/
  index.html      # The full app
  og-image.png    # Social sharing image
  favicon.png     # Browser tab icon
  favicon.ico     # Fallback icon
  robots.txt      # Crawler directives
  sitemap.xml     # Sitemap
vercel.json       # Routing config
```

## Part of

[AI Streamline Hub](https://www.aistreamlinehub.com) — independent research and publishing on AI governance for regulated environments.
