sudo -u postgres psql -c "DROP DATABASE crm"
sudo -u postgres psql -c "CREATE DATABASE crm ENCODING 'UTF-8'"
python manage.py syncdb --noinput
python manage.py migrate
python manage.py load_data
