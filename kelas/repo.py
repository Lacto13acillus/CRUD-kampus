from django.shortcuts import get_object_or_404
from .models import kelas
from dosen.models import dosen
from matakuliah.models import matakuliah

class RepoKelas:
    @staticmethod
    def post(req):
        Dosen = get_object_or_404(dosen, id_dosen=req['id_dosen'])
        Matakuliah = get_object_or_404(matakuliah, id_matkul=req['id_matkul'])

        new_kelas = kelas.objects.create(
            id_kelas=req['id_kelas'], 
            nama_kelas=req['nama_kelas'],
            id_dosen= Dosen,
            id_matkul= Matakuliah
        )
        return {
            'id_kelas': new_kelas.id_kelas,
            'nama_kelas': new_kelas.nama_kelas,
            'id_dosen': Dosen.id_dosen,
            'nama_dosen': Dosen.nama_dosen,
            'nid': Dosen.nid,
            'id_matkul': Matakuliah.id_matkul,
            'sks': Matakuliah.sks
        }
    
    @staticmethod
    def get(kelas_id):
        kelas_update = get_object_or_404(kelas, id_kelas=kelas_id)
        Dosen = kelas_update.id_dosen
        Matakuliah = kelas_update.id_matkul
        
        return {
            'id_kelas': kelas_update.id_kelas,
            'nama_kelas': kelas_update.nama_kelas,
            'id_dosen': Dosen.id_dosen,
            'nid': Dosen.nid,
            'id_matkul': Matakuliah.id_matkul,
            'sks': Matakuliah.sks
        }

    def put(req):
        Kelas = get_object_or_404(kelas, id_kelas=req['id_kelas'])
        Kelas.nama_kelas = req.get('nama_kelas', kelas.nama_kelas)
        Kelas.save()
        return{
            'id_kelas': Kelas.id_kelas,
            'nama_kelas': Kelas.nama_kelas
        }
    
    def delete(req):
        Kelas = get_object_or_404(kelas, id_kelas=req['id_kelas'])
        Kelas.delete()
        return {'message': f"User with id {req['id_kelas']} has been deleted."}