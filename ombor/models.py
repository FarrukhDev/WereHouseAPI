from django.contrib.auth.models import User
from django.db import models

class Ombor(models.Model):
    ism=models.CharField(max_length=50)
    tel=models.CharField(max_length=15)
    ombor_nomi=models.CharField(max_length=30)
    manzil=models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}({self.ombor_nomi})"
