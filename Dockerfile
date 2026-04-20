FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY .env.example ./.env

EXPOSE 8011

CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8011"]
