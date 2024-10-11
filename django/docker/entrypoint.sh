#!/usr/bin/env bash


echo "Generating Migrations"
poetry run python manage.py makemigrations
echo "Done!"

echo "Migrate..."
poetry run  python manage.py migrate --noinput
echo "Migrated!"

echo "Loading fixtures..."
poetry run python manage.py loaddata */fixtures/*.json
echo "Done!"

poetry run python manage.py runserver 0.0.0.0:9000
