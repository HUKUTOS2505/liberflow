# LiberFlow

LiberFlow is LiberCode's internal system for managing technical projects,
employees, sprints, development tasks, Kanban workflow, and time tracking. It
will integrate with the company's cloud Bitrix24 portal while keeping technical
delivery data inside LiberFlow.

The repository is being built in small, verifiable daily packages. Day 1
contains only the Django foundation and a health endpoint. PostgreSQL, Docker,
business entities, the REST API, and Bitrix24 connectivity are intentionally
not implemented yet.

## Requirements

- Python 3.12 or newer
- Git

## Local setup

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python manage.py migrate
python manage.py runserver
```

Bash:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python manage.py migrate
python manage.py runserver
```

The development configuration has safe local defaults. `.env.example`
documents the environment variable contract, but Day 1 does not add an env-file
loader. Export variables in the shell when overriding the defaults. Environment
and PostgreSQL handling will be completed in Day 2.

Open `http://127.0.0.1:8000/health/`. The response is:

```json
{
  "status": "ok"
}
```

## Quality checks

```powershell
python manage.py check
pytest
ruff check .
```

See [ROADMAP.md](ROADMAP.md) for delivery order,
[ARCHITECTURE.md](ARCHITECTURE.md) for system boundaries, and
[PROJECT_STATE.md](PROJECT_STATE.md) for the current handoff state.
