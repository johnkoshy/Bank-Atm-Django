# Django Bank ATM

A Django-based ATM application with login, signup, balance check, deposit, and withdrawal features.

## Setup

1. Clone the repository:
git clone https://github.com/johnkoshy/Bank-Atm-Django.git
cd Bank-Atm-Django

2. Open the project in VS Code (optional):

code .


3. Set up Python:
Ensure Python 3.13.0 is installed. Download from https://www.python.org/downloads/release/python-3130/.
Check "Add Python 3.13 to PATH" during installation.

Verify installation:
python --version

Expected output: Python 3.13.0

Verify pip:
pip --version

4. Set up a virtual environment (recommended):
python -m venv venv
venv\Scripts\activate  # On Windows

On macOS/Linux, use source venv/bin/activate.

5. Install dependencies:
Install Django and MySQL client:
pip install django mysqlclient

If a requirements.txt exists:
pip install -r requirements.txt

6. Set up MySQL database:
Install XAMPP (includes MySQL/MariaDB) from https://www.apachefriends.org/.
Start Apache and MySQL in the XAMPP Control Panel.
Alternatively, install MySQL Community Server from https://dev.mysql.com/downloads/mysql/.
Open http://localhost/phpmyadmin/.
Log in (default: root, password blank or set in XAMPP).
Create a database named djangodb.

Verify MySQL is running on port 3306:
netstat -an | find "3306"

Expected output:
TCP    0.0.0.0:3306           0.0.0.0:0              LISTENING

7. Update Django settings:
Open prj1/settings.py and configure the database:
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

8. Run migrations:
python manage.py makemigrations
python manage.py migrate

9. Collect static files:
python manage.py collectstatic

10. Add test data (optional, for testing login):
python manage.py shell

In the shell:
from ap1.models import Customer
Customer.objects.create(
    username="testuser",
    password="test123",
    customer_name="Test User",
    balance=1000.00
)

11. Start the server:
python manage.py runserver

12. Access the app at http://127.0.0.1:8000.
Test login with testuser/test123.

Features
User signup and login
Balance check
Deposit and withdrawal
Card and type management

Screenshots
## Screenshots
![Dashboard](screenshots/login-screenshot.png)

Database
Uses MySQL (djangodb).
Tables: ap1_customer, ap1_card, ap1_type, ap1_fellow.
Check ap1_customer in phpMyAdmin for customer details.

Requirements
Python 3.13
Django 4.2.3
mysqlclient
XAMPP (MySQL/MariaDB)
