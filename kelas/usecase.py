from .repo import RepoKelas
import uuid
import random
from matakuliah.models import matakuliah
from dosen.models import dosen

class UsecaseKelas:
    @staticmethod
    def post(request):
        Matakuliah = matakuliah.objects.all()
        if not Matakuliah:
            raise ValueError("No categories available")
        
        Dosen = dosen.objects.all()
        if not Dosen:
            raise ValueError("No categories available")
      
        random_matakuliah = random.choice(Matakuliah)
        random_dosen = random.choice(Dosen)
        reqs = {
            'id_kelas': uuid.uuid4(),
            'nama_kelas': request.data['nama_kelas'],
            'id_matkul': random_matakuliah.id_matkul,
            'id_dosen': random_dosen.id_dosen
        }
        dataPost = RepoKelas.post(reqs)
        return dataPost
    
    @staticmethod
    def get(kelas_id):
        dataKelas = RepoKelas.get(kelas_id)
        return dataKelas
    
    def put(request):
        reqs = {
            'id_kelas': request.data['id_kelas'],
            'nama_kelas': request.data.get('nama_kelas'),
        }
        updated_kelas = RepoKelas.put(reqs)
        return updated_kelas
    
    def delete(request):
        reqs = {
            'id_kelas': request.data['id_kelas']
        }
        delete_message = RepoKelas.delete(reqs)
        return delete_message