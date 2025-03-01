from django.db import models
from registrasi.models import registrasi
from django.core.validators import FileExtensionValidator

class nilai(models.Model):
    id_nilai = models.CharField(max_length=60, primary_key=True, unique=True)
    id_registrasi = models.ForeignKey(registrasi, on_delete=models.CASCADE)
    nilai = models.IntegerField(default=0)
    file_nilai = models.ImageField(
        upload_to='nilai/',  # Direktori penyimpanan gambar
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])],
        blank=True, 
        default=""  
        
    )

    def __str__(self):
        return f"{self.id_nilai} - {self.nilai}"
    
