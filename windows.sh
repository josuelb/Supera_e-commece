python -m venv ./venv;
./venv/Scripts/activate;
pip install django django-allauth djangorestframework djangorestframework_simplejwt[crypto] Pillow psycopg2 psycopg2-binary;
cd backend;
python manage.py runserver;