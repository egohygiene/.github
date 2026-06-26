# Reflector

Pass-based organization analysis scaffold.

## Layout

- `engines/audit/` — audit engine entrypoint
- `passes/00_discovery/` — read-only organization discovery pass
- `policies/` — reusable audit policies
- `specs/organization.spec` — organization source-of-truth specification
- `outputs/` — reserved for future derived outputs

## Run

```bash
python reflector/engines/audit/engine.py
```

This writes timestamped artifacts to `.github/audits/<UTC timestamp>/`.
