from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=30,primary_key=True)


class User(models.Model):
    email    = models.EmailField(max_length=30,primary_key=True)
    name     = models.CharField(max_length=25)
    contact  = models.CharField(max_length=11)
    password = models.CharField(max_length=20)

class Product(models.Model):
    Pname       = models.CharField(max_length=20)
    price       = models.IntegerField()
    description = models.TextField(max_length=100)
    cname       = models.ForeignKey(Category,on_delete=models.CASCADE)

class Feedback(models.Model):
    email   =models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=100)

class Cart(models.Model):
    pid   = models.ForeignKey(Product,on_delete = models.CASCADE)
    email = models.ForeignKey(User,on_delete = models.CASCADE)
    qty   = models.SmallIntegerField(default=1)


