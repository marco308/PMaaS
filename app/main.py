from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from app.meetings import get_random_meeting

DESCRIPTION = """\
> *Finally, enterprise-grade infrastructure for your drinking problems.*

---

## What is this?

An API that generates legitimate-sounding business meeting names for pub \
gatherings. Pop one into your calendar and suddenly you're not "going to \
the pub" - you're attending a **Quarterly Pint Review**.

Nobody questions a meeting with a name like that.

---

## Features

| Feature | Status |
|---------|--------|
| Returns a meeting name | ✅ |
| That's it | ✅ |
| Authentication | ❌ We respect your time |
| Database | ❌ Stateless, baby |

---

## Rate Limiting

**5 requests per minute.** If you need more fake meeting names than that, \
you have bigger problems than we can solve.

When you hit the limit, you get cut off. Just like at a real pub.
"""

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(
    title="🍺 PMaaS",
    summary="Pub Meeting as a Service",
    description=DESCRIPTION,
    version="1.0.0",
    contact={
        "name": "Complaints Department",
        "url": "https://github.com/marco308/PMaaS/issues",
    },
    license_info={
        "name": "MIT - Do whatever you want",
        "url": "https://opensource.org/licenses/MIT",
    },
)
app.state.limiter = limiter


def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={
            "error": "Whoa there, slow down! You've been cut off.",
            "message": (
                "The bartender says you've had enough meetings for now. "
                "Try again in a minute."
            ),
        },
    )


app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)


@app.get(
    "/meeting",
    summary="Get a meeting name",
    description=(
        "Returns a single, randomly selected pub meeting name. "
        "Use it wisely. Or don't. We're not your manager."
    ),
    response_description="A very important business meeting name",
    responses={
        200: {
            "description": "A legitimate business meeting",
            "content": {
                "application/json": {
                    "example": {"meeting_name": "Quarterly Pint Review"}
                }
            },
        },
        429: {
            "description": "You've been cut off",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Whoa there, slow down! You've been cut off.",
                        "message": (
                            "The bartender says you've had enough meetings "
                            "for now. Try again in a minute."
                        ),
                    }
                }
            },
        },
    },
)
@limiter.limit("5/minute")
def get_meeting(request: Request):
    return get_random_meeting()
