# Stage 1: Build
FROM python:3.11-slim AS build
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim AS runtime
WORKDIR /app
# Copy the installed dependencies from the build stage
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
# Copy the application code
COPY . /app/
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s CMD curl --fail http://localhost:8000/api/health || exit 1
CMD ["python", "app.py"]