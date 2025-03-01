from django.db import models

class dosen(models.Model):
    id_dosen = models.CharField(max_length=60, primary_key=True, unique=True)
    nama_dosen = models.CharField(max_length=255, unique=True)
    nid = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    