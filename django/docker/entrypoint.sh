#!/usr/bin/env sh


echo "Generating Migrations"
python3 manage.py makemigrations
echo "Done!"

echo "Migrate..."
python3 manage.py migrate --noinput
echo "Migrated!"

echo "Generating translations messages..."
python3 manage.py makemessages -l pt_BR
echo "Trasnslatad generated!"

echo "Compiling messages..."
python3 manage.py compilemessages -v 3
echo "Compiled messages!"

echo "Loading fixtures..."
python3 manage.py loaddata */fixtures/*.json
echo "Done!"

python3 manage.py runserver 0.0.0.0:9000
