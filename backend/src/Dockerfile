FROM python:3.12

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    python3-dev \
    libc-dev \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "app.py"]