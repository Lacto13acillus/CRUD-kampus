from .models import jurusan
from django.shortcuts import get_object_or_404


class Repojurusan():
    def post(req):
        jurusan.objects.create(
            id_jurusan = req['id_jurusan'],
            nama_jurusan = req['nama_jurusan']
        )

        obj = {
            'id_jurusan' : req['id_jurusan']
        }

        return obj
    
    def get(req):
        obj = get_object_or_404(jurusan,
                                id_jurusan = req.data['id_jurusan']
                            )
        
        return obj
    
    def put(req):
        user = get_object_or_404(jurusan, id_jurusan=req['id_jurusan'])
        user.nama_jurusan = req.get('nama_jurusan', user.nama_jurusan)
        user.save()
        return {
            'id_jurusan': user.id_jurusan,
            'nama_jurusan': user.nama_jurusan,
        }
    
    
    def delete(req):
        Jurusan = get_object_or_404(jurusan, id_jurusan=req['id_jurusan'])
        Jurusan.delete()
        return {'message': f"User with id {req['id_jurusan']} has been deleted."}
