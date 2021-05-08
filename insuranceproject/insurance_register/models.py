from django.db import models

# Create your models here.

class insurancetype(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Insurancerecord(models.Model):
    name = models.CharField(max_length=50)
    insurance_id = models.CharField(max_length=8)
    email = models.CharField(max_length=35)
    mobile = models.CharField(max_length=10)
    insurancename = models.CharField(max_length=50)
    insurancetype = models.ForeignKey(insurancetype,on_delete=models.CASCADE)