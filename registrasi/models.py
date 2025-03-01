from django.db import models
import kelas.models as kls
import mahasiswa.models as mhs

class registrasi(models.Model):
    id_registrasi = models.CharField(max_length=60, primary_key=True, unique=True)
    id_kelas = models.ForeignKey(kls.kelas, on_delete=models.CASCADE)
    id_mahasiswa = models.ForeignKey(mhs.mahasiswa, on_delete=models.CASCADE)

