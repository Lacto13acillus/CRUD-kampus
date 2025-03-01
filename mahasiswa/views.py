from rest_framework.decorators import api_view
from rest_framework.response import Response
from .usecase import UsecaseMahasiswa
from rest_framework import status
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes

class ViewMahasiswa():
    @api_view(["POST"])
    def post(request):
        if request.data["nama"] == None or request.data["nama"] == "":
            
            return Response({
                    "code": 400,
                    "message": "nama is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        if request.data["nim"] == None or request.data["nim"] == "":
            
            return Response({
                    "code": 400,
                    "message": "nim is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        if request.data["password"] == None or request.data["password"] == "":
            
            return Response({
                    "code": 400,
                    "message": "nim is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        data = UsecaseMahasiswa.post(request)

        return Response({
                    "code": 200,
                    "message": "sukses",
                    "data": data
        },
        status=status.HTTP_200_OK
        )
    
    @api_view(["GET"])
    @authentication_classes([JWTAuthentication])
    @permission_classes([IsAuthenticated])
    def get(request):
        try:
            # Baca request body sebagai JSON
            body = json.loads(request.body)
            id_mahasiswa = body.get("id_mahasiswa")
            if not id_mahasiswa:
                return Response({
                    "code": 400,
                    "message": "id_mahasiswa is required in request body"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Panggil usecase untuk mendapatkan data
            data = UsecaseMahasiswa.get(id_mahasiswa)
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
        if request.data["id_mahasiswa"] == None or request.data["id_mahasiswa"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = UsecaseMahasiswa.put(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)
    
    @api_view(["DELETE"])
    def delete(request):
        if request.data["id_mahasiswa"] == None or request.data["id_mahasiswa"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = UsecaseMahasiswa.delete(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)
    
    @csrf_exempt  # Nonaktifkan CSRF protection untuk view ini
    @api_view(["POST"])
    def login(request):
        if not request.data.get("nim"):
            return Response({
            "code": 400,
            "message": "nim is required"
        }, status=status.HTTP_400_BAD_REQUEST)
    
        if not request.data.get("password"):
            return Response({
            "code": 400,
            "message": "password is required"
        }, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = UsecaseMahasiswa.login(request)
            return Response({
            "code": 200,
            "message": "success",
            "data": data
        }, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({
            "code": 400,
            "message": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)

    
    
    
