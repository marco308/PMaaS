# PMaaS - Pub Meeting as a Service

[![Tests](https://github.com/YOUR_USERNAME/PMaaS/actions/workflows/test.yml/badge.svg)](https://github.com/YOUR_USERNAME/PMaaS/actions/workflows/test.yml)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

> Finally, enterprise-grade infrastructure for your drinking problems.

## The Problem

You want to go to the pub with your colleagues. But your calendar is a warzone of "syncs" and "alignments" and your manager has hawk-like vision for any empty time slots.

## The Solution

An API that generates legitimate-sounding business meeting names. Pop one of these bad boys into your calendar and suddenly you're not "going to the pub" - you're attending a **Quarterly Pint Review** or conducting an **IPA Impact Assessment**.

Nobody questions a meeting with a name like that.

## Usage

```bash
curl https://your-deployment-url/api/meeting
```

```json
{
  "meeting_name": "Cask Flow Analysis"
}
```

That's it. That's the whole API. We didn't overcomplicate this.

## Features

- Returns a meeting name
- That's the feature
- There's only one endpoint
- We didn't add authentication because we respect your time
- Rate limited to 5 requests/minute because honestly if you need more than 5 fake meeting names per minute, you have bigger problems

## Rate Limiting

Hit the API too many times and you'll get:

```json
{
  "error": "Whoa there, slow down! You've been cut off.",
  "message": "The bartender says you've had enough meetings for now. Try again in a minute."
}
```

Just like a real pub.

## Self-Hosting

```bash
docker compose up --build
```

Now you have your own personal meeting name generator running on port 8000. Your IT department will be so proud.

## Development

You want to contribute to this masterpiece? Brave.

```bash
# Install dependencies
poetry install

# Run the dev server
poetry run uvicorn app.main:app --reload

# Run tests
poetry run pytest
```

The dev server runs on `http://localhost:8000`. There's also auto-generated docs at `/docs` if you're into that sort of thing.

## FAQ

**Q: Is this production ready?**
A: It's a single endpoint that returns random strings. Yes. This is as production ready as it gets.

**Q: Can I contribute new meeting names?**
A: Sure, open a PR. Bad puns only.

**Q: Why does this exist?**
A: Because "drinks with the team" kept getting declined but "Stakeholder Aleignment" hasn't failed yet.

**Q: Is this GDPR compliant?**
A: We don't store anything. We don't even know who you are. We don't want to know.

## License

[MIT](LICENSE). Do whatever you want with it.
