from rest_framework.decorators import api_view
from rest_framework.response import Response
from .usecase import UsecaseMatkul
from rest_framework import status
import json

class ViewMatkul():
    @api_view(["POST"])
    def post(request):
        if request.data["nama_matkul"] == None or request.data["nama_matkul"] == "":
            
            return Response({
                    "code": 400,
                    "message": "nama_matkul is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        if request.data["sks"] == None or request.data["sks"] == "":
            
            return Response({
                    "code": 400,
                    "message": "sks is required",
                    
                            },
                            status=status.HTTP_400_BAD_REQUEST
                            )
        
        data = UsecaseMatkul.post(request)

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
            id_matkul = body.get("id_matkul")
            if not id_matkul:
                return Response({
                    "code": 400,
                    "message": "id_matkul is required in request body"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Panggil usecase untuk mendapatkan data
            data = UsecaseMatkul.get(id_matkul)
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
        if request.data["id_matkul"] == None or request.data["id_matkul"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = UsecaseMatkul.put(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)
    
    @api_view(["DELETE"])
    def delete(request):
        if request.data["id_matkul"] == None or request.data["id_matkul"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = UsecaseMatkul.delete(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)
