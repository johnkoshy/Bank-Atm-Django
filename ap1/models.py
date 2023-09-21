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

    def __str__(self):
        return self.customer_name

    class Meta:
        db_table = 'customer'
        verbose_name_plural = "Customer"


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "customer"


class Card(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ap1_card'
        verbose_name_plural = "Card"


class Type(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ap1_type'
        verbose_name_plural = "Type"


class Fellow(models.Model):
    name = models.CharField(max_length=124)
    email = models.CharField(max_length=125)
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, blank=True, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ap1_fellow'
        verbose_name_plural = "Fellow"
