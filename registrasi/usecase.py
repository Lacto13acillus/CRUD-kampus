from .repo import RepoRegistrasi
import uuid

class UsecaseRegistrasi:
    @staticmethod
    def post(request):
        reqs = {
            'id_registrasi': uuid.uuid4(),
            'id_kelas': request.data['id_kelas'],
            'id_mahasiswa': request.data['id_mahasiswa']
        }
        dataPost = RepoRegistrasi.post(reqs)
        return dataPost
    
    @staticmethod
    def get(id_registrasi):
        dataRegistrasi = RepoRegistrasi.get(id_registrasi)
        return dataRegistrasi
    
    @staticmethod
    def put(request):
        reqs = {
            'id_registrasi': request.data['id_registrasi'],
            'id_kelas': request.data.get('id_kelas'),
            'id_mahasiswa': request.data.get('id_mahasiswa')
        }
        updated_registrasi = RepoRegistrasi.put(reqs)
        return updated_registrasi
    
    @staticmethod
    def delete(request):
        reqs = {
            'id_registrasi': request.data['id_registrasi']  # Pastikan ini adalah dictionary
        }
        delete_message = RepoRegistrasi.delete(reqs)
        return delete_message