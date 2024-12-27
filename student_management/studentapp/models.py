from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    usertype= models.CharField(max_length=30)

class Teachernew(models.Model):
    teacher_id=models.ForeignKey(user,on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    phone_number=models.IntegerField()
class Studentnew(models.Model):
    student_id=models.ForeignKey(user,on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    phone_num=models.IntegerField()