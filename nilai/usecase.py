from .repo import RepoNilai
import uuid
import random
from registrasi.models import registrasi

class UsecaseNilai:
    @staticmethod
    def post(request):
        Registrasi = registrasi.objects.all()
        if not Registrasi:
            raise ValueError("No categories available")
        
        if 'file_nilai' not in request.FILES:
            raise ValueError("File is required.")
      
        random_registrasi = random.choice(Registrasi)
        reqs = {
            'id_nilai': uuid.uuid4(),
            'nilai': request.data['nilai'],
            'id_registrasi': random_registrasi.id_registrasi,
            'file_nilai': request.FILES['file_nilai']  # Ambil file dari request
        }
        dataPost = RepoNilai.post(reqs)
        return dataPost
    
    @staticmethod
    def get(nilai_id):
        dataMatkul = RepoNilai.get(nilai_id)
        return dataMatkul
    
    def put(request):
        reqs = {
            'id_nilai': request.data['id_nilai'],
            'nilai': request.data.get('nilai'),
        }
        updated_user = RepoNilai.put(reqs)
        return updated_user
    
    def delete(request):
        reqs = {
            'id_nilai': request.data['id_nilai']
        }
        delete_message = RepoNilai.delete(reqs)
        return delete_message