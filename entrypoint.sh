#!/bin/bash
set -e

echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate --noinput

echo "Loading fixtures..."
python manage.py loaddata fixtures/payments/item.json

echo "Collecting static files..."
python manage.py collectstatic --noinput

exec "$@"
