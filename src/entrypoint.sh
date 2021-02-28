#!/bin/sh

echo "Waiting for postgres..."
until psql postgres://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME -c '\l'; do
    echo "Postgres is unavailable - sleeping"
    sleep 2
done

echo "Postgres is up - continuing"

# Collect static files
echo “Collect static files”
python manage.py collectstatic --noinput

# Apply database migrations
echo “Apply database migrations”
python manage.py migrate


exec "$@"