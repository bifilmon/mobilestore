from django.db import models

# Create your models here.

class Mobile(models.Model):
    model_name = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    available_stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images",null=True)


