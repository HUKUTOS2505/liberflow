# Security

## Baseline policy

- No secrets, real access tokens, webhook URLs, database passwords, or customer
  data may enter Git.
- `.env` files are ignored; `.env.example` contains placeholders only.
- Production must use a strong external `DJANGO_SECRET_KEY`, `DEBUG=false`,
  explicit allowed hosts, HTTPS, secure cookies, and trusted proxy settings.
- Authorization is deny-by-default and must be tested at both endpoint and
  object level when business data is introduced.
- Validate uploaded files, limit size and type, and store them outside source
  control when attachments are implemented.
- Treat Bitrix24 and browser input as untrusted. Validate identifiers, payload
  shape, state transitions, and callback authenticity.
- Logs and synchronization records must be useful without exposing credentials
  or unnecessary personal data.

## Current package

Day 1 has no production deployment and no external credentials. The fallback
secret in development settings is intentionally unsuitable for production.
Production settings and Django deployment checks belong to later deployment
packages.

## Reporting

Report suspected vulnerabilities privately to the LiberCode project owner. Do
not open a public issue containing exploit details, secrets, or personal data.
Rotate exposed credentials immediately and remove them from active systems;
rewriting Git history requires an explicit incident response decision.
