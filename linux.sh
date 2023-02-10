python3 -m venv ./venv;
source ./venv/bin/activate;
pip3 install django django-allauth djangorestframework djangorestframework_simplejwt[crypto] Pillow psycopg2 psycopg2-binary;
cd backend;
python3 manage.py runserver;