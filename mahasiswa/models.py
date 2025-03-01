from django.db import models
import jurusan.models as jrs

class mahasiswa(models.Model):
    id_mahasiswa = models.CharField(max_length=60, primary_key=True, unique=True)
    id_jurusan = models.ForeignKey(jrs.jurusan, on_delete=models.CASCADE)
    nama = models.CharField(max_length=60, unique=True)
    nim = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True, blank=True)  

    def get_user_id(self):
        return self.id_mahasiswa