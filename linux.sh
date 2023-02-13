python3 -m venv ./venv;
source ./venv/bin/activate;
pip3 install django django-allauth;
pip3 install djangorestframework djangorestframework_simplejwt[crypto];
pip3 install Pillow psycopg2 psycopg2-binary;
pip3 install django-cors-headers;
cd backend;
python3 manage.py runserver;
