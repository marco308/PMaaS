# Stage 1: export pinned runtime deps from poetry.lock (Poetry stays out of the final image)
FROM python:3.12-slim AS builder

RUN pip install --no-cache-dir poetry poetry-plugin-export

WORKDIR /build
COPY pyproject.toml poetry.lock ./
RUN poetry export --only main --format requirements.txt --output requirements.txt

# Stage 2: the actual pub
FROM python:3.12-slim

LABEL org.opencontainers.image.title="PMaaS" \
      org.opencontainers.image.description="Pub Meeting as a Service" \
      org.opencontainers.image.source="https://github.com/marco308/PMaaS" \
      org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

COPY --from=builder /build/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# pyproject.toml is read at runtime for the API version
COPY pyproject.toml ./
COPY app/ ./app/

RUN useradd --create-home --uid 1000 barkeep
USER barkeep

EXPOSE 8000

# /openapi.json isn't rate limited, unlike /api/meeting
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/openapi.json', timeout=2)"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
