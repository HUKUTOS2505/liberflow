# Testing

LiberFlow uses pytest and pytest-django. Ruff provides static lint checks.
Tests should describe observable behavior and protect permissions, domain
invariants, service transactions, and integration mappings as those features are
introduced.

## Run locally

```powershell
.\.venv\Scripts\Activate.ps1
python manage.py check
pytest
ruff check .
```

The current suite verifies that `GET /health/` returns HTTP 200 with exactly
`{"status": "ok"}`. The health route confirms process-level HTTP readiness; it
does not claim that future dependencies such as PostgreSQL or Bitrix24 are
healthy.

## Conventions

- Put cross-application and HTTP behavior tests under `tests/`.
- Keep focused app tests close to their application when the app grows.
- Name files `test_*.py` and avoid order-dependent tests.
- Prefer factories or small builders over opaque shared fixtures once models
  exist.
- Mock the network at the Bitrix24 client boundary; unit and CI tests never call
  the real company portal.
- Every permission rule and workflow transition needs positive and negative
  coverage.
- Database-specific behavior must run against PostgreSQL after package 2.
