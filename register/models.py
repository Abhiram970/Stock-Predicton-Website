from django.db import models

# Create your models here.
class page2(models.Model):
    UserID = models.CharField(max_length=100)
    password = models.CharField(max_length=50) 