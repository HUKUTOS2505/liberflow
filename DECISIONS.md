# Architecture decisions

## ADR-001: Modular Django monolith

- **Status:** Accepted
- **Decision:** Build one Django deployment organized into focused domain apps.
- **Why:** LiberFlow needs consistent permissions and transactions more than
  independent service scaling. A monolith reduces operational overhead and
  supports incremental delivery.
- **Consequence:** Domain ownership and import direction must remain explicit so
  the monolith does not become one coupled module.

## ADR-002: Source-of-truth split with Bitrix24

- **Status:** Accepted
- **Decision:** Treat Bitrix24 as authoritative for CRM companies, contacts,
  deals, and CRM managers; treat LiberFlow as authoritative for technical
  delivery data.
- **Why:** It prevents two systems from competing over the same facts.
- **Consequence:** CRM records in LiberFlow are projections with stable external
  identifiers, synchronization metadata, and visible conflicts.

## ADR-003: Explicit services for business workflows

- **Status:** Accepted
- **Decision:** Put multi-model workflows and external effects behind explicit
  services rather than relying on Django signals.
- **Why:** Call sites, transactions, errors, and tests remain understandable.
- **Consequence:** Thin views do not imply an unnecessary repository or command
  framework; services are introduced only when behavior needs them.

## ADR-004: Server-rendered UI plus REST API

- **Status:** Accepted
- **Decision:** Use Django templates for the internal MVP interface and Django
  REST Framework for programmatic access, without a separate SPA.
- **Why:** It delivers usable screens with less frontend and deployment
  complexity while preserving an API boundary.
- **Consequence:** Interactive features such as Kanban should use focused
  progressive enhancement instead of duplicating the product in a second app.

## ADR-005: SQLite only for Day 1 bootstrap

- **Status:** Superseded by package 2 when completed
- **Decision:** Use Django's SQLite configuration only to verify the initial
  project before PostgreSQL and Docker are introduced in the next package.
- **Why:** Day 1 explicitly excludes PostgreSQL and Docker.
- **Consequence:** No business migrations or production-like database behavior
  should be built against SQLite. PostgreSQL becomes the supported database in
  package 2.

## ADR-006: Supported Python and Django baseline

- **Status:** Accepted
- **Decision:** Require Python 3.12+ and use the Django 5.2 LTS release line.
- **Why:** The combination provides a current Python baseline and a stable,
  long-supported Django foundation.
- **Consequence:** Tooling targets Python 3.12 syntax even when development uses
  a newer interpreter.
