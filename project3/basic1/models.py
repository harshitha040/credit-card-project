from django.db import models

# Create your models here.
class ccard_info(models.Model):
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=100)
    cc_number=models.CharField(max_length=300)
    limit=models.FloatField()
    outstanding=models.FloatField(default=0)
    
   
