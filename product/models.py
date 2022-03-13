from django.db import models
from ombor.models import Ombor


class Product(models.Model):
    nom = models.CharField(max_length=20)
    narx = models.CharField(max_length=15)
    miqdor = models.IntegerField()
    brend_nomi = models.CharField(max_length=20)
    omborxona = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

