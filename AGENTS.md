# AGENTS.md

## Mission

Build LiberFlow as a real internal LiberCode product and a maintainable Python
backend portfolio project. Work incrementally and preserve the architecture
already documented in the repository.

## Working rules

- Complete one daily package per session and stop after its commit.
- Do not start later roadmap packages early.
- Use Python 3.12+, Django, Django REST Framework, PostgreSQL, pytest,
  pytest-django, Ruff, Docker, and Docker Compose in their planned packages.
- Do not add Celery, Redis, microservices, or a separate SPA during MVP.
- Keep secrets out of source code, logs, fixtures, documentation, and Git.
- Never use Git date environment variables or create backdated commits.
- Never push without explicit user instruction.
- Prefer explicit service calls over Django signals for business workflows.
- Keep models and views focused; move substantial business logic to services.
- Preserve the CRM/technical-delivery source-of-truth boundary.

## Package completion checklist

1. Run `python manage.py check`.
2. Run `pytest`.
3. Run `ruff check .`.
4. Review `git status` and ensure no secrets or generated files are staged.
5. Update documentation, `PROJECT_STATE.md`, and `CHANGELOG.md`.
6. Create one meaningful commit only when all checks pass.
7. Stop without beginning the next package.

## Application boundaries

- `accounts`: authentication, users, roles, permissions.
- `employees`: profiles, positions, skills.
- `clients`: LiberFlow projections of Bitrix24 companies and contacts.
- `projects`: technical projects, memberships, sprints.
- `tasks`: tasks, workflow, comments, attachments, time tracking, history.
- `notifications`: in-product notifications and preferences.
- `integrations`: Bitrix24 client, synchronization, webhooks, sync journal.
- `common`: genuinely shared infrastructure without domain ownership.

Do not create cross-application imports casually. Domain writes should be
owned by the relevant application and orchestrated through explicit services.
