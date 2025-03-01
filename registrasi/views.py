from rest_framework.decorators import api_view
from rest_framework.response import Response
from .usecase import UsecaseRegistrasi
from rest_framework import status
import json

class ViewRegistrasi:
    @api_view(["POST"])
    def post(request):
        if not request.data.get("id_kelas"):
            return Response({
                "code": 400,
                "message": "id_kelas is required"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.data.get("id_mahasiswa"):
            return Response({
                "code": 400,
                "message": "id_mahasiswa is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = UsecaseRegistrasi.post(request)
            return Response({
                "code": 200,
                "message": "success",
                "data": data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "code": 400,
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(["GET"])
    def get(request):
        try:
            # Baca request body sebagai JSON
            body = json.loads(request.body)
            id_matkul = body.get("id_registrasi")
            if not id_matkul:
                return Response({
                    "code": 400,
                    "message": "id_registrasi is required in request body"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Panggil usecase untuk mendapatkan data
            data = UsecaseRegistrasi.get(id_matkul)
            return Response({
                "code": 200,
                "message": "sukses",
                "data": data
            }, status=status.HTTP_200_OK)
        except json.JSONDecodeError:
            return Response({
                "code": 400,
                "message": "Invalid JSON in request body"
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "code": 404,
                "message": str(e)
            }, status=status.HTTP_404_NOT_FOUND)
        

        
    @api_view(["PUT"])
    def put(request):
        if not request.data.get("id_registrasi"):
            return Response({
                "code": 400,
                "message": "id_registrasi is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = UsecaseRegistrasi.put(request)
            return Response({
                "code": 200,
                "message": "success",
                "data": data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "code": 400,
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(["DELETE"])
    def delete(request):
        if not request.data.get("id_registrasi"):
            return Response({
                "code": 400,
                "message": "id_registrasi is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = UsecaseRegistrasi.delete(request)
            return Response({
                "code": 200,
                "message": "success",
                "data": data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "code": 400,
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
