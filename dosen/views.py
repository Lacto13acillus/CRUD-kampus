from rest_framework.decorators import api_view
from rest_framework.response import Response
from .usecase import Usecasedosen
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

class ViewDosen():
    @api_view(["POST"])
    def post(request):
        if request.data["nama_dosen"] == None or request.data["nama_dosen"] == "":
            
            return Response({
                    "code": 400,
                    "message": "name_dosen is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        if request.data["nid"] == None or request.data["nid"] == "":
            
            return Response({
                    "code": 400,
                    "message": "nid is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        if request.data["password"] == None or request.data["password"] == "":
            
            return Response({
                    "code": 400,
                    "message": "nid is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        data = Usecasedosen.post(request)

        return Response({
                    "code": 200,
                    "message": "sukses",
                    "data": data
        },
        status=status.HTTP_200_OK
        )
    
    @api_view(["GET"])
    def get(request):
        if request.data["id_dosen"] == None or request.data["id_dosen"] == "":
            
            return Response({
                    "code": 400,
                    "message": "id is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )  
        
        data = Usecasedosen.get(request)

        return Response({
                    "code": 200,
                    "message": "sukses",
                    "data": data
        },
        status=status.HTTP_200_OK
        )

    @api_view(["PUT"])
    def put(request):
        if request.data["id_dosen"] == None or request.data["id_dosen"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = Usecasedosen.put(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK) 
    
    @api_view(["DELETE"])
    def delete(request):
        if request.data["id_dosen"] == None or request.data["id_dosen"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = Usecasedosen.delete(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)
    
    @csrf_exempt  # Nonaktifkan CSRF protection untuk view ini
    @api_view(["POST"])
    def login(request):
        if not request.data.get("nid"):
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
            data = Usecasedosen.login(request)
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
