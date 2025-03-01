from django.db import models
import matakuliah.models as mtk
import dosen.models as dsn

class kelas(models.Model):
    id_kelas = models.CharField(max_length=60, primary_key=True, unique=True)
    id_matkul = models.ForeignKey(mtk.matakuliah, on_delete=models.CASCADE)
    nama_kelas = models.CharField(max_length=60, unique=True)
    id_dosen = models.ForeignKey(dsn.dosen, on_delete=models.CASCADE)
