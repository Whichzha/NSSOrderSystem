from django.db import models

# Create your models here.

class Merchantdaccount(models.Model):  #商家账号信息
    mid = models.AutoField(primary_key = True)
    merName = models.CharField(max_length=12)
    merPassword = models.CharField(max_length=12)

