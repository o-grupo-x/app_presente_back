FROM python:3.11

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Health check to verify the app is running
HEALTHCHECK --interval=30s --timeout=3s CMD curl --fail http://localhost:8000/api/health || exit 1

CMD ["python", "app.py"]