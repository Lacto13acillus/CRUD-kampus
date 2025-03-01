from .repo import Repojurusan
import uuid

class Usecasejurusan():
    def post(req):
        reqs = {
            'id_jurusan' : uuid.uuid4 (),
            'nama_jurusan' : req.data['nama_jurusan'],
        }
        data = Repojurusan.post(reqs)
        return data
    
    def get(req):
        dataJurusan = Repojurusan.get(req)
        data = {
            'id_jurusan': dataJurusan.id_jurusan,
            'nama_jurusan': dataJurusan.nama_jurusan,
        }
        return data
    
    def put(request):
        reqs = {
            'id_jurusan': request.data['id_jurusan'],
            'name': request.data.get('nama_jurusan'),
        }
        updated_user = Repojurusan.put(reqs)
        return updated_user
    
    def delete(request):
        reqs = {
            'id_jurusan': request.data['id_jurusan']
        }
        delete_message = Repojurusan.delete(reqs)
        return delete_message