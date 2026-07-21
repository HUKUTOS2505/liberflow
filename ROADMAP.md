# LiberFlow roadmap

Each numbered item is one daily package. A session completes only one item,
runs all quality checks, updates project state, creates one commit, and stops.

1. **Architecture and Django initialization.** Establish documentation,
   settings, `common`, health check, pytest, and Ruff.
2. **PostgreSQL, Docker Compose, and environment settings.** Add PostgreSQL,
   containerized local development, validated environment configuration, and
   database readiness checks.
3. **Users, roles, and permissions.** Introduce the custom user model before
   business migrations and define MVP authorization roles.
4. **Employee profiles, positions, and skills.** Model staff data and skill
   assignments independently from authentication.
5. **Clients, projects, and participants.** Add local client projections,
   technical projects, and project membership.
6. **Tasks, types, and priorities.** Add tasks and subtasks with focused
   reference models and validation.
7. **Statuses, workflow, and transition history.** Make allowed state changes
   explicit and auditable through services.
8. **Sprints and planning.** Add sprint lifecycle, backlog assignment, and
   capacity-oriented planning foundations.
9. **Comments, watchers, and attachments.** Add technical collaboration while
   enforcing access and file-safety constraints.
10. **Time tracking.** Record work logs, estimates, and project/task rollups.
11. **Django Admin.** Provide safe, useful internal administration for the
   implemented domains.
12. **REST API.** Add Django REST Framework serializers, viewsets, routing, and
   schema foundations.
13. **API permissions, filtering, and search.** Enforce object visibility and
   make project/task discovery practical.
14. **Web interface.** Add server-rendered navigation, project, sprint, and task
   screens without a separate SPA.
15. **Kanban board.** Implement workflow-aware board interactions and ordering.
16. **Notifications and personal dashboard.** Add in-product events,
   preferences, and actionable personal views.
17. **Bitrix24 REST client.** Add an authenticated, timeout-aware client with
   configuration, error mapping, and contract tests; no production secret in Git.
18. **Import Bitrix24 deals and clients.** Synchronize CRM-owned companies,
   contacts, deals, and manager references into local projections.
19. **Create a LiberFlow project from a deal.** Add an idempotent explicit
   conversion workflow while retaining Bitrix24 identifiers.
20. **Send project progress to Bitrix24.** Publish approved technical progress
   summaries without moving technical ownership into CRM.
21. **Incoming Bitrix24 events.** Validate and process supported webhook events
   idempotently.
22. **Synchronization journal and manual retries.** Expose sanitized attempts,
   outcomes, correlation data, and safe operator retries.
23. **Full testing.** Expand unit, integration, permissions, workflow, and
   synchronization coverage; document testing risks.
24. **CI and security checks.** Add GitHub Actions and dependency/security
   verification with protected secret handling.
25. **Production Docker and deployment.** Create production images, runtime
   checks, static handling, operational instructions, backup, and rollback plan.
26. **Demo data, screenshots, and final documentation.** Prepare a scrubbed
   portfolio demonstration and complete operator/developer handoff.

Roadmap details can change through an explicit decision record, but package
ordering protects foundational decisions such as creating a custom user model
before domain data exists.
