# Stage 1 - Install build dependencies
FROM python:3.12-alpine AS builder
WORKDIR /app
RUN python -m venv .venv && .venv/bin/pip install --no-cache-dir -U pip setuptools
COPY requirements.txt .
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

# Stage 2 - Copy only necessary files to the runner stage
FROM python:3.12-alpine
LABEL org.opencontainers.image.source https://github.com/0x6flab/chatgpt-zuri
WORKDIR /app
COPY --from=builder /app /app
COPY messages ./messages
COPY app.py .
ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "app.py"]