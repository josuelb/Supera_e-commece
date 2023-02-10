python -m venv ./venv;
./venv/Scripts/activate;
pip install django djangorestframework djangorestframework_simplejwt[crypto] Pillow;
cd backend;
python manage.py runserver;