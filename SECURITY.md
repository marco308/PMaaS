# Security Policy

> Even pubs have bouncers.

## The Reality Check

Let's be honest: this is an API that returns random strings about fake meetings. We're not storing your data, we're not handling payments, and we're definitely not protecting state secrets.

That said, we still care about security. If you've found something, let us know.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |
| older   | :x: Just update, it's one endpoint |

## Reporting a Vulnerability

**Please do not open public issues for security vulnerabilities.**

Instead, report security issues by emailing the maintainers directly or through GitHub's private vulnerability reporting feature.

When reporting, please include:

1. **Description** - What's the issue?
2. **Steps to reproduce** - How can we see it?
3. **Impact** - What could go wrong? (Remember, we just return meeting names)
4. **Suggested fix** - If you have one

## What We Consider Security Issues

- Remote code execution (please no)
- Server-side request forgery
- Injection vulnerabilities
- Anything that could affect users of the API

## What We Don't Consider Security Issues

- Rate limiting bypasses (you really need more than 5 meeting names per minute?)
- The meeting names being too funny
- Denial of service via excessive laughter

## Response Timeline

We'll try to respond to security reports within 48 hours. For a single-endpoint joke API, we think that's pretty reasonable.

## Acknowledgments

We appreciate responsible disclosure. If you report a valid security issue, we'll:
- Credit you in the fix (unless you prefer to stay anonymous)
- Buy you a virtual pint
- Add your name to a hypothetical security hall of fame that we might create someday

---

*Remember: with great power comes great responsibility. And this API has very little power, so we should all be fine.*
