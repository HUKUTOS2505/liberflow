# Bitrix24 integration

## Scope and status

The company portal is `https://sitepro.bitrix24.ru`. No live connection,
webhook, token, client, or CRM data is included in daily package 1.

The integration is scheduled for packages 17 through 22. Until then, domain
models must not assume that a remote call is always available or that technical
delivery data belongs in Bitrix24.

## Data ownership

Bitrix24 owns companies, contacts, deals, and CRM managers. LiberFlow owns
technical projects, sprints, tasks, technical statuses, Kanban, technical
comments, time tracking, and development history.

Local CRM projections will retain the Bitrix24 entity type and stable external
ID. Mapping must be explicit and idempotent. Deletion and conflict policy will
be decided from Bitrix24 API behavior before import implementation.

## Planned flows

1. Import supported companies, contacts, deals, and manager references.
2. Create one LiberFlow technical project explicitly from an eligible deal.
3. Send a constrained project-progress summary back to Bitrix24.
4. Receive and validate supported Bitrix24 events.
5. Record sanitized synchronization attempts and allow safe manual retries.

## Security requirements

- Store webhook URLs, tokens, and credentials only in deployment secrets.
- Never commit or print credentials, full request headers, or sensitive payloads.
- Use HTTPS, finite connection/read timeouts, and bounded retries.
- Validate incoming event authenticity using the mechanism supported by the
  selected Bitrix24 integration method.
- Apply least privilege to the Bitrix24 application or webhook.
- Redact secrets and personal data from synchronization logs.
- Test the transport using fakes or mocked HTTP; automated tests must not call
  the company portal.

The exact authentication method and endpoint contracts will be documented from
current official Bitrix24 documentation during package 17.
