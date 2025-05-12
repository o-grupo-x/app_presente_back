######################
# Etapa 1: Build
######################
FROM python:3.11-slim AS builder

WORKDIR /app

# Evita prompts interativos
ENV DEBIAN_FRONTEND=noninteractive

# Instala dependências do sistema necessárias para compilar pacotes Python com dependências nativas
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Instala dependências Python no diretório temporário
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt

######################
# Etapa 2: Runtime
######################
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copia somente os pacotes necessários da etapa de build
COPY --from=builder /install /usr/local

# Copia o código da aplicação
COPY . .

EXPOSE 8000

# Healthcheck opcional
HEALTHCHECK --interval=30s --timeout=3s CMD curl --fail http://localhost:8000/api/health || exit 1

CMD ["python", "app.py"]