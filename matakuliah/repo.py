from django.shortcuts import get_object_or_404
from .models import matakuliah
from dosen.models import dosen

class RepoMatkul:
    @staticmethod
    def post(req):
        Dosen = get_object_or_404(dosen, id_dosen=req['id_dosen'])

        new_matakuliah = matakuliah.objects.create(
            id_matkul=req['id_matkul'], 
            nama_matkul=req['nama_matkul'],
            sks=req['sks'],
            id_dosen= Dosen 
        )
        return {
            'id_matkul': new_matakuliah.id_matkul,
            'nama_matkul': new_matakuliah.nama_matkul,
            'sks': new_matakuliah.sks,
            'id_dosen': Dosen.id_dosen,
            'nama_dosen': Dosen.nama_dosen,
            'nid': Dosen.nid

        }
    
    @staticmethod
    def get(matkul_id):
        matakuliah_update = get_object_or_404(matakuliah, id_matkul=matkul_id)
        Dosen = matakuliah_update.id_dosen  # Ambil data dosen terkait
        
        return {
            'id_matkul': matakuliah_update.id_matkul,
            'nama_matkul': matakuliah_update.nama_matkul,
            'sks': matakuliah_update.sks,
            'id_dosen': Dosen.id_dosen,
            'nama_dosen': Dosen.nama_dosen,
            'nid': Dosen.nid
        }

    def put(req):
        Matakuliah = get_object_or_404(matakuliah, id_matkul=req['id_matkul'])
        Matakuliah.nama_matkul = req.get('nama_matkul', matakuliah.nama_matkul)
        Matakuliah.sks = req.get('sks', matakuliah.sks)
        Matakuliah.save()
        return{
            'id_matkul': Matakuliah.id_matkul,
            'nama_matkul': Matakuliah.nama_matkul,
            'sks': Matakuliah.sks
        }
    
    def delete(req):
        Matakuliah = get_object_or_404(matakuliah, id_matkul=req['id_matkul'])
        Matakuliah.delete()
        return {'message': f"User with id {req['id_matkul']} has been deleted."}