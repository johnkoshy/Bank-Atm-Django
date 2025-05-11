# Django Bank ATM

A Django-based ATM application with login, signup, balance check, deposit, and withdrawal features.

## Setup

1. Clone the repository:
git clone https://github.com/johnkoshy/Bank-Atm-Django.git
cd Bank-Atm-Django

text

Copy

2. Open the project in VS Code (optional):
code .

text

Copy

3. Set up Python:
Ensure Python 3.13.0 is installed. Download from https://www.python.org/downloads/release/python-3130/.
Check "Add Python 3.13 to PATH" during installation.

Verify installation:
python --version

text

Copy
Expected output: Python 3.13.0

Verify pip:
pip --version

text

Copy

4. Set up a virtual environment (recommended):
python -m venv venv
venv\Scripts\activate  # On Windows

text

Copy
On macOS/Linux, use `source venv/bin/activate`.

5. Install dependencies:
Install Django, MySQL client, and phonenumber-field:
pip install django mysqlclient django-phonenumber-field

text

Copy
If a `requirements.txt` exists:
pip install -r requirements.txt

text

Copy

6. Set up MySQL database:
Install XAMPP (includes MySQL/MariaDB) from https://www.apachefriends.org/.
Start Apache and MySQL in the XAMPP Control Panel.
Alternatively, install MySQL Community Server from https://dev.mysql.com/downloads/mysql/.
Open http://localhost/phpmyadmin/.
Log in (default: root, password blank or set in XAMPP).
Create a database named `djangodb`.

Verify MySQL is running on port 3306:
netstat -an | find "3306"

text

Copy
Expected output:
TCP    0.0.0.0:3306           0.0.0.0:0              LISTENING

text

Copy

7. Update Django settings:
Open `bankproject/settings.py` and configure the database:
```python
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
Run migrations:
text

Copy
python manage.py makemigrations
python manage.py migrate
Collect static files:
text

Copy
python manage.py collectstatic
Add test data (optional, for testing login):
text

Copy
python manage.py shell
In the shell:

python

Copy
from bankapp.models import Customer
Customer.objects.create(
    username="testuser",
    password="test123",
    customer_name="Test User",
    balance=1000.00
)
Hash passwords:
text

Copy
python bankproject/hash_passwords.py
Start the server:
text

Copy
python manage.py runserver
Access the app at http://127.0.0.1:8000. Test login with testuser/test123.
Features
User signup and login
Balance check
Deposit and withdrawal
Card and type management
Phone activation
Screenshots
Database
Uses MySQL (djangodb).
Tables: customer, bankapp_user, bankapp_card, bankapp_type, bankapp_fellow.
Check customer in phpMyAdmin for customer details.

Requirements
Python 3.13
Django 4.2.3
mysqlclient
django-phonenumber-field
XAMPP (MySQL/MariaDB)