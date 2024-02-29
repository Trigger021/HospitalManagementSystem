from django.db import models

# Create your models here.


class Users(models.Model):
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    yearofbirth = models.DateField(null=True)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Member(models.Model):
    Username = models.CharField(max_length=100)
    Email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.Username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


