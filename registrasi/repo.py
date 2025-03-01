from django.shortcuts import get_object_or_404
from .models import registrasi
from kelas.models import kelas
from mahasiswa.models import mahasiswa
import kelas.models as kls
import mahasiswa.models as mhs
class RepoRegistrasi:
    @staticmethod
    def post(req):
        kelasReq = get_object_or_404(kls.kelas, id_kelas=req['id_kelas'])
        Mahasiswa = get_object_or_404(mhs.mahasiswa, id_mahasiswa=req['id_mahasiswa'])

        new_registrasi = registrasi.objects.create(
            id_registrasi=req['id_registrasi'], 
            id_kelas= kelasReq,
            id_mahasiswa= Mahasiswa
        )
        return {
            'id_registrasi': new_registrasi.id_registrasi,
            'id_kelas': {
                'id_kelas': kelasReq.id_kelas,
                'nama_kelas': kelasReq.nama_kelas
            },
            'id_mahasiswa': {
                'id_mahasiswa': Mahasiswa.id_mahasiswa,
                'nama': Mahasiswa.nama,
                'nim': Mahasiswa.nim
            }
        }
    
    @staticmethod
    def get(registrasi_id):
        registrasi_update = get_object_or_404(registrasi, id_registrasi=registrasi_id)
        kelasReq = registrasi_update.id_kelas
        Mahasiswa = registrasi_update.id_mahasiswa
        
        return {
            'id_registrasi': registrasi_update.id_registrasi,
            'id_kelas': {
                'id_kelas': kelasReq.id_kelas,
                'nama_kelas': kelasReq.nama_kelas
            },
            'id_mahasiswa': {
                'id_mahasiswa': Mahasiswa.id_mahasiswa,
                'nama': Mahasiswa.nama,
                'nim': Mahasiswa.nim
            }
        }

    def put(req):
        Registrasi = get_object_or_404(registrasi, id_registrasi=req['id_registrasi'])

        if 'id_kelas' in req:
            Kelas = get_object_or_404(kls.kelas, id_kelas=req['id_kelas'])
            Registrasi.id_kelas = Kelas
        if 'id_mahasiswa' in req:
            Mahasiswa = get_object_or_404(mhs.mahasiswa, id_mahasiswa=req['id_mahasiswa'])
            Registrasi.id_mahasiswa = Mahasiswa
        
        Registrasi.save()
        return {
            'id_registrasi': Registrasi.id_registrasi,
            'id_kelas': {
                'id_kelas': Registrasi.id_kelas.id_kelas,
                'nama_kelas': Registrasi.id_kelas.nama_kelas
            },
            'id_mahasiswa': {
                'id_mahasiswa': Registrasi.id_mahasiswa.id_mahasiswa,
                'nama': Registrasi.id_mahasiswa.nama,
                'nim': Registrasi.id_mahasiswa.nim
            }
        }
    

    @staticmethod
    def delete(req):
        # Ambil id_registrasi dari dictionary req
        id_registrasi = req.get('id_registrasi')
        if not id_registrasi:
            raise ValueError("id_registrasi is required")
        
        # Hapus data registrasi
        registrasi_data = get_object_or_404(registrasi, id_registrasi=id_registrasi)
        registrasi_data.delete()
        return {'message': f"Registrasi dengan id {id_registrasi} berhasil dihapus."}