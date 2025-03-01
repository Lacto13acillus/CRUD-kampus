from .repo import Repodosen
import uuid

class Usecasedosen():
    def post(req):
        reqs = {
            'id_dosen' : uuid.uuid4 (),
            'nama_dosen' : req.data['nama_dosen'],
            'nid': req.data['nid'],
            'password': req.data['password']
        }
        data = Repodosen.post(reqs)
        return data
    
    def get(req):
        dataDosen = Repodosen.get(req)
        data = {
            'id_dosen': dataDosen.id_dosen,
            'nama_dosen': dataDosen.nama_dosen,
            'nid': dataDosen.nid,
        }
        return data
    
    def put(request):
        reqs = {
            'id_dosen': request.data['id_dosen'],
            'nama_dosen': request.data.get('nama_dosen'),
            'nid': request.data.get('nid')
        }
        updated_user = Repodosen.put(reqs)
        return updated_user
    
    def delete(request):
        reqs = {
            'id_dosen': request.data['id_dosen']
        }
        delete_message = Repodosen.delete(reqs)
        return delete_message
    
    @staticmethod
    def login(request):
        reqs = {
            'nid': request.data['nid'],
            'password': request.data['password']
        }
        dataLogin = Repodosen.login(reqs)
        return dataLogin