from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(models.Model):
    real_name=models.CharField(max_length=200)
    tz=models.CharField(max_length=200)


    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    user=models.ForeignKey(User,related_name='activity_periods',on_delete=models.CASCADE)
    start_time=models.CharField(max_length=50)
    end_time=models.CharField(max_length=50)

    def __str__(self):
        return str(self.start_time)+"---"+str(self.end_time)