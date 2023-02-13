python -m venv ./venv;
./venv/Scripts/activate;
pip install django django-allauth
pip install djangorestframework djangorestframework_simplejwt[crypto]
pip install Pillow psycopg2 psycopg2-binary;
pip install django-cors-headers
cd backend;
python manage.py runserver;