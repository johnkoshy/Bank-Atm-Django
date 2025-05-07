# bankproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bankapp.urls')),  # Update to bankapp.urls if needed
]