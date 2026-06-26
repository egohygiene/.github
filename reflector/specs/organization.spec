{
  "organization": {
    "name": "egohygiene",
    "description": "Organization-wide standards, templates, and developer experience",
    "default_branch": "main"
  },
  "repositories": [
    {
      "name": ".github",
      "path": ".",
      "purpose": "Organization profile, standards, and shared defaults"
    }
  ],
  "audit": {
    "engine": "reflector.audit",
    "version": "0.1.0",
    "output_root": ".github/audits",
    "passes": [
      "00_discovery"
    ]
  },
  "enabled_policies": [
    "documentation"
  ],
  "extensions": {
    "future_pass_inputs": {},
    "future_policy_overrides": {}
  }
}
