from pathlib import Path

p = Path("public/index.html")
text = p.read_text(encoding="utf-8")

required = [
    "2 December 2027",
    "2 August 2028",
    "Creditworthiness Review Agent",
    "ART. 27 — FRIA · ART. 26(9) — DPIA SUPPORT",
    "Measures are defined to support AI literacy",
    "completedCount / 5",
    "[agent, maturity, boundary, oversight, suspension, accountability, audit]",
    "Named backup",
    "Reach / contact path",
    "Tested / rehearsed",
    "FRAMEWORK ACCOUNTABILITY ROLES · OVERSIGHT OWNER SUPPORTS ART. 26(2)",
]

for item in required:
    assert item in text, f"Missing required hygiene fix: {item}"

for forbidden in [
    "Aug 2026 enforcement risk is concrete",
    "Sanctions Triage Agent",
    "Workers interacting with or overseen by the system must receive appropriate training (Art. 4)",
    "Annex IV documentation pack assembled for conformity assessment file",
    "completedCount / 4",
]:
    assert forbidden not in text, f"Stale or incorrect content remains: {forbidden}"

print("Workspace hygiene static checks: PASS")
