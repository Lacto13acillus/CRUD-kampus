from django.shortcuts import get_object_or_404
from .models import mahasiswa
from jurusan.models import jurusan
from rest_framework_simplejwt.tokens import RefreshToken

class RepoMahasiswa:
    @staticmethod
    def post(req):
        Jurusan = get_object_or_404(jurusan, id_jurusan=req['id_jurusan'])

        new_mahasiswa = mahasiswa.objects.create(
            id_mahasiswa=req['id_mahasiswa'], 
            nama=req['nama'],
            nim=req['nim'],
            id_jurusan=Jurusan,
            password=req['password']  # Tambahkan password
        )
        return {
            'id_mahasiswa': new_mahasiswa.id_mahasiswa,
            'nama': new_mahasiswa.nama,
            'nim': new_mahasiswa.nim,
            'id_jurusan': Jurusan.id_jurusan,
            'nama_jurusan': Jurusan.nama_jurusan
        }
    
    @staticmethod
    def get(mahasiswa_id):
        mahasiswa_update = get_object_or_404(mahasiswa, id_mahasiswa=mahasiswa_id)
        Jurusan = mahasiswa_update.id_jurusan  # Ambil data jurusan terkait
        
        return {
            'id_mahasiswa': mahasiswa_update.id_mahasiswa,
            'nama': mahasiswa_update.nama,
            'nim': mahasiswa_update.nim,
            'id_jurusan': Jurusan.id_jurusan,
            'nama_jurusan': Jurusan.nama_jurusan,
        }

    @staticmethod
    def put(req):
        Mahasiswa = get_object_or_404(mahasiswa, id_mahasiswa=req['id_mahasiswa'])
        Mahasiswa.nama = req.get('nama', Mahasiswa.nama)
        Mahasiswa.nim = req.get('nim', Mahasiswa.nim)
        Mahasiswa.save()
        return {
            'id_mahasiswa': Mahasiswa.id_mahasiswa,
            'nama': Mahasiswa.nama,
            'nim': Mahasiswa.nim
        }
    
    @staticmethod
    def delete(req):
        Mahasiswa = get_object_or_404(mahasiswa, id_mahasiswa=req['id_mahasiswa'])
        Mahasiswa.delete()
        return {'message': f"User with id {req['id_mahasiswa']} has been deleted."}

    @staticmethod
    def login(req):
        nim = req.get('nim')
        password = req.get('password')
        
        # Cari mahasiswa berdasarkan nim
        try:
            mahasiswa_data = mahasiswa.objects.get(nim=nim)
        except mahasiswa.DoesNotExist:
            raise ValueError("NIM tidak ditemukan")
        
        # Periksa password
        if mahasiswa_data.password != password:
            raise ValueError("Password salah")
        
        # Jika berhasil, buat JWT token
        refresh = RefreshToken.for_user(mahasiswa_data)
        
        return {
            'id_mahasiswa': mahasiswa_data.id_mahasiswa,
            'nama': mahasiswa_data.nama,
            'nim': mahasiswa_data.nim,
            'id_jurusan': mahasiswa_data.id_jurusan.id_jurusan,
            'nama_jurusan': mahasiswa_data.id_jurusan.nama_jurusan,
            'tokens': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }