from rest_framework.decorators import api_view
from rest_framework.response import Response
from .usecase import Usecasejurusan
from rest_framework import status

class ViewJurusan():
    @api_view(["POST"])
    def post(request):
        if request.data["nama_jurusan"] == None or request.data["nama_jurusan"] == "":
            
            return Response({
                    "code": 400,
                    "message": "name is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        data = Usecasejurusan.post(request)

        return Response({
                    "code": 200,
                    "message": "sukses",
                    "data": data
        },
        status=status.HTTP_200_OK
        )
    
    @api_view(["GET"])
    def get(request):
        if request.data["id_jurusan"] == None or request.data["id_jurusan"] == "":
            
            return Response({
                    "code": 400,
                    "message": "id is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )  
        
        data = Usecasejurusan.get(request)

        return Response({
                    "code": 200,
                    "message": "sukses",
                    "data": data
        },
        status=status.HTTP_200_OK
        )

    @api_view(["PUT"])
    def put(request):
        if request.data["id_jurusan"] == None or request.data["id_jurusan"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = Usecasejurusan.put(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK) 
    
    @api_view(["DELETE"])
    def delete(request):
        if request.data["id_jurusan"] == None or request.data["id_jurusan"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = Usecasejurusan.delete(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)

