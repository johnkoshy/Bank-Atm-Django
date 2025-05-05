import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bankproject.settings')

import django
django.setup()

from django.contrib.auth.hashers import make_password
from bankapp.models import Customer

customers = Customer.objects.all()
for customer in customers:
    if not customer.password.startswith('pbkdf2_sha256$'):
        customer.password = make_password(customer.password)
        customer.save()

print("Passwords hashed successfully!")