Django Bank ATM
A Django-based ATM application with user authentication, balance checks, deposits, withdrawals, and card management.
Features

Secure signup and login with password hashing
Real-time balance inquiries
Deposit and withdrawal transactions
Card and type management
Phone number activation

Setup

Clone the Repository:
git clone https://github.com/johnkoshy/Bank-Atm-Django.git
cd Bank-Atm-Django


Install Python 3.13:

Download from Python 3.13.0.
Check "Add Python to PATH" during installation.
Verify: python --version (should output Python 3.13.0).


Set Up Virtual Environment:
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux


Install Dependencies:
pip install django mysqlclient django-phonenumber-field


Set Up MySQL:

Install XAMPP or MySQL.
Start MySQL, access phpMyAdmin, and create a database named djangodb.
Verify port: netstat -an | find "3306" (should show DNS).


Configure Database:Edit bankproject/settings.py:
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


Run Migrations:
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic


Add Test Data (Optional):
python manage.py shell

Run:
from bankapp.models import Customer
from django.contrib.auth.hashers import make_password
Customer.objects.create(
    username="testuser",
    password=make_password("test123"),
    customer_name="Test User",
    balance=1000.00
)


Hash Passwords:
python bankproject/hash_passwords.py


Start Server:
python manage.py runserver

Access at http://127.0.0.1:8000 with testuser/test123.


Screenshots

Caption: Login interface of the Django Bank ATM.
Troubleshooting

"Table 'djangodb.customer' doesn't exist":
Ensure djangodb exists in phpMyAdmin.
Recreate: Drop djangodb, recreate it, and run python manage.py migrate.


Migration Issues:python manage.py migrate bankapp zero --fake
python manage.py migrate bankapp



Requirements

Python 3.13
Django 4.2.3
mysqlclient
django-phonenumber-field
XAMPP or MySQL

