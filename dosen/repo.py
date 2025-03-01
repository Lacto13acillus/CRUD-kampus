from .models import dosen
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken


class Repodosen():
    def post(req):
        dosen.objects.create(
            id_dosen = req['id_dosen'],
            nama_dosen = req['nama_dosen'],
            nid = req['nid'],
            password=req["password"]

        )

        obj = {
            'id_dosen' : req['id_dosen']
        }

        return obj
    
    def get(req):
        obj = get_object_or_404(dosen,
                                id_dosen = req.data['id_dosen']
                            )
        
        return obj
    
    def put(req):
        user = get_object_or_404(dosen, id_dosen=req['id_dosen'])
        user.nama_dosen = req.get('nama_dosen', user.nama_dosen)
        user.nid = req.get('nid', user.nid)
        user.save()
        return {
            'id_dosen': user.id_dosen,
            'nama_dosen': user.nama_dosen,
            'nid': user.nid,
        }
    
    
    def delete(req):
        Jurusan = get_object_or_404(dosen, id_dosen=req['id_dosen'])
        Jurusan.delete()
        return {'message': f"User with id {req['id_dosen']} has been deleted."}
    
    @staticmethod
    def login(req):
        nid = req.get('nid')
        password = req.get('password')
        
        # Cari mahasiswa berdasarkan nim
        try:
            dosen_data = dosen.objects.get(nid=nid)
        except dosen.DoesNotExist:
            raise ValueError("NID tidak ditemukan")
        
        # Periksa password
        if dosen_data.password != password:
            raise ValueError("Password salah")
        
        # Jika berhasil, buat JWT token
        refresh = RefreshToken.for_user(dosen_data)
        
        return {
            'id_dosen': dosen_data.id_dosen,
            'nama_dosen': dosen_data.nama_dosen,
            'nid': dosen_data.nid,
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }