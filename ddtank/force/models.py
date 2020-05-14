from django.db import models


class Ddtank(models.Model):
    loai = models.CharField(max_length=50)
    khoangcach = models.FloatField(max_length=10)
    docao = models.FloatField(max_length=10)
    gio = models.FloatField(max_length=10)
    goc = models.FloatField(max_length=10)
    luc = models.FloatField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
