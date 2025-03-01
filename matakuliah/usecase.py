from .repo import RepoMatkul
import uuid
import random
from dosen.models import dosen

class UsecaseMatkul:
    @staticmethod
    def post(request):
        Dosen = dosen.objects.all()
        if not Dosen:
            raise ValueError("No categories available")
      
        random_matkul = random.choice(Dosen)
        reqs = {
            'id_matkul': uuid.uuid4(),
            'nama_matkul': request.data['nama_matkul'],
            'sks': request.data['sks'],
            'id_dosen': random_matkul.id_dosen
        }
        dataPost = RepoMatkul.post(reqs)
        return dataPost
    
    @staticmethod
    def get(matkul_id):
        dataMatkul = RepoMatkul.get(matkul_id)
        return dataMatkul
    
    def put(request):
        reqs = {
            'id_matkul': request.data['id_matkul'],
            'nama_matkul': request.data.get('nama_matkul'),
            'sks': request.data.get('sks')
        }
        updated_user = RepoMatkul.put(reqs)
        return updated_user
    
    def delete(request):
        reqs = {
            'id_matkul': request.data['id_matkul']
        }
        delete_message = RepoMatkul.delete(reqs)
        return delete_message
        
