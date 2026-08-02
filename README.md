# Agentic Governance Profile Builder

**Live:** [workspace.aistreamlinehub.com](https://workspace.aistreamlinehub.com)

Build a structured governance profile for one AI agent, mapped to EU AI Act Article 26 deployer obligations — in under fifteen minutes.

## What it does

Six named primitives, applied to a single agent. There is no seventh — the Governance Profile and Gap Register are outputs, not primitives.

| Primitive | What it produces |
|---|---|
| P-01 — Decision Boundary Contract | Allowed, prohibited, and conditional action lists |
| P-02 — Oversight Trigger Matrix | Per-action oversight level and entry conditions |
| P-03 — Accountability Canvas | Four-owner mapping with gap diagnostic |
| P-04 — Audit Schema (Handoff Receipt) | Handoff receipt template and retention guidance |
| P-05 — Gap Register | Prioritised remediation list, exportable |
| P-06 — Suspension Authority Ledger | Named authority, trigger conditions, and notification chain |

A preceding Maturity Check produces a structural gap score across six governance dimensions but is not itself one of the six primitives.

**Output:** Governance Profile (PDF) + Gap Register (CSV). Not legal advice — a documentation aid only.

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
