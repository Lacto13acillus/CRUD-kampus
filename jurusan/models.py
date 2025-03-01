from django.db import models

class jurusan(models.Model):
    id_jurusan = models.CharField(max_length=255,primary_key=True, unique=True)
    nama_jurusan = models.CharField(max_length=255, unique=True)


    
    