# Contributing to PMaaS

> Welcome to the pub. First round's on us.

Thanks for considering a contribution to PMaaS! Whether you're here to add a terrible pun, fix a bug, or improve the docs, we appreciate you pulling up a barstool.

## House Rules

1. **Keep it fun** - This is a joke project with real code standards.
2. **Bad puns only** - If you're adding meeting names, they must be pub-themed and groan-worthy.
3. **Don't be a jerk** - See our [Code of Conduct](CODE_OF_CONDUCT.md). We're all here to have a good time.

## How to Contribute

### Adding Meeting Names

The easiest way to contribute! Open `app/meetings.py` and add your masterpiece to the `MEETINGS` list.

**Good examples:**

- "Stakeholder Aleignment"
- "Sprint Retrospective"

**Bad examples:**

- "Team Meeting" (boring, no pun)
- "Let's get wasted" (too on the nose, HR will notice)

### Reporting Bugs

Found something broken? [Open an issue](../../issues/new?template=bug_report.md). Include:

- What you expected to happen
- What actually happened
- How many pints you'd had (optional but appreciated)

### Suggesting Features

Got an idea? [Open a feature request](../../issues/new?template=feature_request.md). Keep in mind this is intentionally a single-endpoint API. We're not adding authentication, databases, or blockchain integration.

## Development Setup

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/PMaaS.git
cd PMaaS

# Install dependencies
poetry install

# Run the dev server
poetry run uvicorn app.main:app --reload

# Run tests (do this before submitting PRs)
poetry run pytest

# Check your code style
poetry run ruff check .
poetry run ruff format .
```

## Pull Request Process

1. **Fork the repo** and create your branch from `main`
2. **Write your code** - keep it simple, we're not building a spaceship
3. **Run the tests** - `poetry run pytest`
4. **Run the linter** - `poetry run ruff check .` and `poetry run ruff format .`
5. **Open a PR** - fill out the template, we'll review it over a pint

### PR Guidelines

- Keep PRs small and focused (one feature/fix per PR)
- Write a clear description of what you changed and why
- If you're adding meeting names, bulk additions are fine
- Don't worry about being perfect - we'll work through it together

## Code Style

- We use [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
- Python 3.12+
- 88 character line limit
- Type hints are nice but not required for this project

## Questions?

Open an issue or find us at the pub. Cheers! 🍺
