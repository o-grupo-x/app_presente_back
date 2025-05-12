# ----------------------------
# Stage 1: Build - Usa uma imagem mais completa para a instalação das dependências
# ----------------------------

FROM python:3.11-slim AS build

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de requisitos para o contêiner
COPY requirements.txt /app/

# Instala as dependências necessárias para o ambiente de build  
RUN pip install -r requirements.txt

RUN pip install flask

# ----------------------------
# Stage 2: Runtime - Usa uma imagem mais enxuta para rodar a aplicação
# ----------------------------

FROM python:3.11-slim AS runtime

# Define o diretório de trabalho
WORKDIR /app

# Copia as dependências instaladas do estágio de build
COPY --from=build /app /app/

# Copia o código da aplicação
COPY . /app/

# Exponhe a porta necessária para o app
EXPOSE 8000

# Health check para garantir que o app está funcionando corretamente
HEALTHCHECK --interval=30s --timeout=3s CMD curl --fail http://localhost:8000/api/health || exit 1

# Comando para iniciar o app
CMD ["python", "app.py"]
