FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir gunicorn whitenoise

COPY . .

RUN mkdir -p db && \
    python manage.py makemigrations main && \
    python manage.py migrate && \
    python manage.py create_default_superuser && \
    python manage.py collectstatic --noinput

EXPOSE 1407

CMD gunicorn --bind 0.0.0.0:1407 root.wsgi:application --workers 3