# Architecture

## System context

LiberFlow is a Django modular monolith backed by PostgreSQL. It serves a
server-rendered internal interface and a REST API from one deployable
application. This shape keeps transactions, permissions, testing, and operation
simple while the product and team are small.

Bitrix24 at `https://sitepro.bitrix24.ru` is an external system. Integration
must use configuration supplied outside Git, explicit application services,
timeouts, idempotency, and a sanitized synchronization journal.

## Ownership boundary

Bitrix24 is the source of truth for:

- CRM companies;
- contacts;
- deals;
- CRM managers.

LiberFlow is the source of truth for:

- technical projects and project membership;
- sprints and development planning;
- tasks, subtasks, priorities, and technical workflow states;
- Kanban ordering;
- technical comments and time records;
- development history and internal notifications.

LiberFlow stores local projections and external identifiers for CRM-owned data.
It does not silently overwrite CRM ownership. Synchronization conflicts must be
visible and retryable.

## Modular monolith

The planned Django applications are:

- `accounts`: identity, roles, and permission policy;
- `employees`: employee profiles, positions, and skills;
- `clients`: local projections of CRM clients and contacts;
- `projects`: technical projects, participants, and sprints;
- `tasks`: tasks, workflow, collaboration, audit history, and time records;
- `notifications`: in-product notifications and preferences;
- `integrations`: Bitrix24 transport, mapping, synchronization, and journal;
- `common`: small cross-cutting primitives and operational endpoints.

Applications own their models and mutations. Views and API endpoints validate
transport input, then call model methods or application services. Multi-model
business processes belong in a service layer and use explicit transactions.
Django signals are reserved for framework-level decoupling, not the main
business workflow.

## Runtime boundaries

The MVP deploys as a single Django process plus PostgreSQL. Docker Compose is
for reproducible local operation and later production packaging. Long-running
background infrastructure is excluded from MVP; synchronization begins as
explicit, bounded requests or management commands and can be redesigned only
when measured requirements justify it.

## Settings

`config/settings/base.py` contains environment-independent settings.
`config/settings/development.py` contains local overrides. Additional test and
production settings will be added when their deployment needs exist. Secrets
and environment-specific host/database values are never committed.

## MVP boundary

MVP includes users and roles, employee metadata, clients, projects, project
membership, sprints, tasks/subtasks, workflow, Kanban, technical collaboration,
time tracking, audit history, notifications, REST API, server-rendered UI, and
the defined Bitrix24 synchronization flows.

MVP excludes Celery, Redis, microservices, a separate SPA, generalized workflow
engines, real-time websockets, billing, payroll, HR document management, and
arbitrary integration platforms. These are not forbidden forever; they require
observed product needs and an architecture decision.
