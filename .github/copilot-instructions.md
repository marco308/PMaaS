# Copilot Instructions for PMaaS

## Project Overview

PMaaS (Pub Meeting as a Service) is a FastAPI microservice with a single endpoint that returns random pub-themed meeting names. Intentionally minimal: stateless, no database, no auth.

## Architecture

```
app/main.py      → FastAPI app, rate limiting (slowapi), `/api` router prefix
app/meetings.py  → MEETINGS list + get_random_meeting() function
tests/test_api.py → API tests using FastAPI TestClient
```

**Key design decisions:**

- Version is read dynamically from `pyproject.toml` using `tomllib`
- Rate limiting: 5 req/min per IP via slowapi (returns 429 with pub-themed message)
- Single endpoint: `GET /api/meeting` → `{"meeting_name": "..."}`

## Development Commands

```bash
poetry install                              # Install dependencies
poetry run uvicorn app.main:app --reload    # Dev server (http://localhost:8000)
poetry run pytest                           # Run all tests
poetry run pytest --cov=app                 # Tests with coverage
poetry run ruff check .                     # Lint
poetry run ruff format .                    # Format
poetry run ruff check --fix .               # Auto-fix lint issues
docker compose up --build                   # Run in Docker
```

## Code Conventions

- **Python 3.12+** with Ruff linting (rules: E, F, I, UP)
- **88-char line limit**, imports sorted automatically
- **Commit messages**: Follow [Conventional Commits](https://conventionalcommits.org) - used by python-semantic-release for versioning
  - `feat:` → minor version bump
  - `fix:`, `perf:` → patch version bump
- **No type hints required** but welcome

## Testing Patterns

Tests use `FastAPI TestClient` with no mocking. See [tests/test_api.py](../tests/test_api.py):

- Test response status codes and JSON structure
- Verify meeting names are from the `MEETINGS` list
- Rate limit test exhausts 6 requests to trigger 429

## Adding Meeting Names

Edit `app/meetings.py` - add pub-themed puns to the `MEETINGS` list. Examples of the style:

- "Stakeholder Aleignment" (ale pun)
- "Cask Flow Analysis" (cash flow pun)
- "IPA Impact Assessment" (business jargon pun)

## CI/CD Pipeline

- **test.yml**: Runs on PRs to main - lint, format check, pytest with Codecov upload
- **release.yml**: Semantic release on main branch pushes
- PRs require passing checks before merge
