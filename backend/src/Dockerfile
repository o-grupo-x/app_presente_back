FROM python:3.11-slim AS builder

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt


FROM python:3.11-slim AS runtime

WORKDIR /app

ENV PYTHONPATH=/usr/local

COPY --from=builder /install /usr/local
COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s CMD curl --fail http://localhost:8000/api/health || exit 1

LABEL build_time=$(date)

CMD ["python", "app.py"]