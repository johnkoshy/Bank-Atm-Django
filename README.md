# Django Bank ATM

A Django-based ATM application with login, signup, balance check, deposit, and withdrawal features.

## Setup

1. Clone the repository:
git clone https://github.com/johnkoshy/Bank-Atm-Django.git
cd Bank-Atm-Django

2. Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Set up MySQL database:
Install XAMPP and start Apache and MySQL.
Open http://localhost/phpmyadmin/.
Create a database named djangodb.
Update prj1/settings.py with your database credentials if different:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

5. Run migrations:
python manage.py migrate

6. Collect static files:
python manage.py collectstatic

7. Start the server:
python manage.py runserver

8. Access the app at http://127.0.0.1:8000.

Features:
User signup and login
Balance check
Deposit and withdrawal
Card and type management

## Screenshots
![Dashboard](screenshots/login-screenshot.png)

Database:
Uses MySQL (djangodb).
Tables: ap1_customer, ap1_card, ap1_type, ap1_fellow.
Check ap1_customer in phpMyAdmin for customer details.

Requirements:
Python 3.13
Django 4.2.3
PyMySQL
XAMPP (MySQL)
