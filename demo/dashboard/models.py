from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    id_number = models.CharField(max_length=10)
    profession = models.CharField(max_length=20)
    married = models.BooleanField()
    city = models.CharField(max_length=30)
    birth = models.DateField(null=True, blank=True)

class Delivery(models.Model):
    timestamp = models.TimeField()
    orderid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=10)
    order = models.CharField(max_length=50)



