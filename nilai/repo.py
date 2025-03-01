from django.shortcuts import get_object_or_404
from .models import nilai
from registrasi.models import registrasi
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError 

class RepoNilai:
    @staticmethod
    def post(req):
        allowed_extensions = ["jpg", "jpeg", "png", "gif"]
        
        # Cek apakah file ada dalam request
        if "file_nilai" not in req:
            raise ValidationError("file_nilai is required.")

        file_nilai = req["file_nilai"]
        file_extension = file_nilai.name.split(".")[-1].lower()  # Ambil ekstensi file

        # Validasi ekstensi file
        if file_extension not in allowed_extensions:
            raise ValidationError("Invalid file format. Only JPEG, PNG, and GIF are allowed.")
        
        Registrasi = get_object_or_404(registrasi, id_registrasi=req['id_registrasi'])

        new_nilai = nilai.objects.create(
                id_nilai=req['id_nilai'], 
                nilai=req['nilai'],
                id_registrasi=Registrasi,
                file_nilai=req.get('file_nilai', None)  
            )
        return {
                'id_nilai': new_nilai.id_nilai,
                'nilai': new_nilai.nilai,
                'id_registrasi': Registrasi.id_registrasi,
                'file_nilai': new_nilai.file_nilai.url if new_nilai.file_nilai else None
            }
    
    @staticmethod
    def get(nilai_id):
        nilai_update = get_object_or_404(nilai, id_nilai=nilai_id)
        Registrasi = nilai_update.id_registrasi  # Ambil data dosen terkait
        
        return {
            'id_nilai': nilai_update.id_nilai,
            'nilai': nilai_update.nilai,
            'file_nilai': nilai_update.file_nilai.url,
            'id_registrasi': Registrasi.id_registrasi         
        }

    def put(req):
        Nilai = get_object_or_404(nilai, id_nilai=req['id_nilai'])
        Nilai.nilai = req.get('nilai', nilai.nilai)
        Nilai.save()
        return{
            'id_nilai': Nilai.id_nilai,
            'nilai': Nilai.nilai
        }
    
    def delete(req):
        Nilai = get_object_or_404(nilai, id_nilai=req['id_nilai'])
        Nilai.delete()
        return {'message': f"User with id {req['id_nilai']} has been deleted."}