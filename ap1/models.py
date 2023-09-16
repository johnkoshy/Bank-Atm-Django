from django.db import models


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=20)
    deposit = models.IntegerField()
    withdrawal = models.IntegerField()
    balance = models.IntegerField()
    account_number = models.IntegerField()

    class Meta:
        db_table = 'customer'


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username