# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> Or as we call it: Keep a Bar Tab.

## [Unreleased]

### Added
- Nothing yet. Buy us a pint and we might add something.

---

## [1.1.0] - 2026-01-14

### Added
- Documentation files: CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md
- Updated .gitignore for deployment files (docker-stack.yml, deploy.sh)

### Changed
- Refactored API routes to use `/api` prefix for cleaner structure
- Updated tests to match new endpoint paths
- **Dependencies:**
  - fastapi: ^0.115.0 → ^0.128.0
  - httpx: ^0.27.0 → ^0.28.1
  - uvicorn: ^0.32.0 → ^0.40.0
  - pytest: ^8.0.0 → ^9.0.2
  - ruff: ^0.8.0 → ^0.14.11
- **Docker:** Python 3.12-slim → 3.14-slim
- **CI/CD:**
  - actions/checkout: 4 → 6
  - actions/setup-python: 5 → 6
  - actions/cache: 4 → 5

### Fixed
- Test badge URL in README.md

---

## [1.0.0] - 2024-01-14

### Added
- Initial release - the pub is open!
- Single endpoint: `GET /api/meeting` returns a random pub-themed meeting name
- Rate limiting: 5 requests/minute (we're not animals)
- Docker support for self-hosting
- Sarcastic error messages when rate limited
- This changelog (you're reading it)

### Security
- No authentication required (you're welcome)
- No data stored (GDPR compliant by virtue of not caring who you are)

---

## Release Name Conventions

Because we're committed to the bit:

| Version | Codename |
|---------|----------|
| 1.0.0   | "First Round" |
| 1.1.0   | "Second Round" |
| 2.0.0   | TBD |

---

*"The only thing better than a changelog is an open bar."*
*— Someone, probably*
