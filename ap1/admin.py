from django.contrib import admin
from .models import Customer

from ap1.models import Type, Card, Fellow


# Register your models here.
admin.site.register(Customer)

admin.site.register(Type)
admin.site.register(Card)
admin.site.register(Fellow)
