from django.db import models
import dosen.models as dsn

class matakuliah(models.Model):
    id_matkul = models.CharField(max_length=60, primary_key=True, unique=True)
    id_dosen = models.ForeignKey(dsn.dosen, on_delete=models.CASCADE)
    nama_matkul = models.CharField(max_length=60, unique=True)
    sks = models.IntegerField(default=0)