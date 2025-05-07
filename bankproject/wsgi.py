# bankproject/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bankproject.settings')  # Updated from prj1.settings to bankproject.settings

application = get_wsgi_application()