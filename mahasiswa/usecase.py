from .repo import RepoMahasiswa
import uuid
import random
from jurusan.models import jurusan

class UsecaseMahasiswa:
    @staticmethod
    def post(request):
        Jurusan = jurusan.objects.all()
        if not Jurusan:
            raise ValueError("No categories available")
      
        random_jurusan = random.choice(Jurusan)
        reqs = {
            'id_mahasiswa': uuid.uuid4(),
            'nama': request.data['nama'],
            'nim': request.data['nim'],
            'id_jurusan': random_jurusan.id_jurusan,
            'password': request.data['password']  # Tambahkan password
        }
        dataPost = RepoMahasiswa.post(reqs)
        return dataPost
    
    @staticmethod
    def get(mahasiswa_id):
        dataMahasiswa = RepoMahasiswa.get(mahasiswa_id)
        return dataMahasiswa
    
    @staticmethod
    def put(request):
        reqs = {
            'id_mahasiswa': request.data['id_mahasiswa'],
            'nama': request.data.get('nama'),
            'nim': request.data.get('nim')
        }
        updated_user = RepoMahasiswa.put(reqs)
        return updated_user
    
    @staticmethod
    def delete(request):
        reqs = {
            'id_mahasiswa': request.data['id_mahasiswa']
        }
        delete_message = RepoMahasiswa.delete(reqs)
        return delete_message

    @staticmethod
    def login(request):
        reqs = {
            'nim': request.data['nim'],
            'password': request.data['password']
        }
        dataLogin = RepoMahasiswa.login(reqs)
        return dataLogin