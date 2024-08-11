from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class accounts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    userName = models.CharField(max_length=20)
    userEmail = models.EmailField()
    phone = models.IntegerField(null=True)
    userGender = models.CharField(max_length=6,null=True)
    joinedDate = models.DateField(null=True)