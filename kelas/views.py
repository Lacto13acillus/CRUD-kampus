from rest_framework.decorators import api_view
from rest_framework.response import Response
from .usecase import UsecaseKelas
from rest_framework import status
import json

class ViewKelas():
    @api_view(["POST"])
    def post(request):
        if request.data["nama_kelas"] == None or request.data["nama_kelas"] == "":
            
            return Response({
                    "code": 400,
                    "message": "nama is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        data = UsecaseKelas.post(request)

        return Response({
                    "code": 200,
                    "message": "sukses",
                    "data": data
        },
        status=status.HTTP_200_OK
        )
    
    @api_view(["GET"])
    def get(request):
        try:
            # Baca request body sebagai JSON
            body = json.loads(request.body)
            id_kelas = body.get("id_kelas")
            if not id_kelas:
                return Response({
                    "code": 400,
                    "message": "id_kelas is required in request body"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Panggil usecase untuk mendapatkan data
            data = UsecaseKelas.get(id_kelas)
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
        if request.data["id_kelas"] == None or request.data["id_kelas"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = UsecaseKelas.put(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)
    
    @api_view(["DELETE"])
    def delete(request):
        if request.data["id_kelas"] == None or request.data["id_kelas"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = UsecaseKelas.delete(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)
