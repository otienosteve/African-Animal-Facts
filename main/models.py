from django.db import models

# Create your models here.
# Animal Facts


class Animal(models.Model):
    animal=models.CharField(max_length=45)
    fact=models.CharField(max_length=500)
    source=models.CharField(max_length=80)
