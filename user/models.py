from django.db import models
from ombor.models import Ombor

class Client(models.Model):
    ism=models.CharField(max_length=35)
    tel=models.CharField(max_length=15)
    dokon_nomi=models.CharField(max_length=25)
    manzil=models.CharField(max_length=50)
    omborxona=models.ForeignKey(Ombor,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ism}({self.dokon_nomi})"
