from rest_framework.decorators import api_view
from rest_framework.response import Response
from .usecase import UsecaseNilai
from rest_framework import status
import json
from django.core.exceptions import ValidationError

class ViewNilai():
    @api_view(["POST"])
    def post(request):
        if request.data.get("nilai") is None or request.data["nilai"] == "":
            return Response({
                "code": 400,
                "message": "nilai is required",
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = UsecaseNilai.post(request)
            return Response({
                "code": 200,
                "message": "sukses",
                "data": data
            }, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({
                "code": 400,
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
            return Response({
                "code": 400,
                "message": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @api_view(["GET"])
    def get(request):
        try:
            # Baca request body sebagai JSON
            body = json.loads(request.body)
            id_nilai = body.get("id_nilai")
            if not id_nilai:
                return Response({
                    "code": 400,
                    "message": "id_nilai is required in request body"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Panggil usecase untuk mendapatkan data
            data = UsecaseNilai.get(id_nilai)
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
        if request.data["id_nilai"] == None or request.data["id_nilai"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = UsecaseNilai.put(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)
    
    @api_view(["DELETE"])
    def delete(request):
        if request.data["id_nilai"] == None or request.data["id_nilai"] == "":
            return Response({
                "code": 400,
                "message": "ID is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        data = UsecaseNilai.delete(request)
        return Response({
            "code": 200,
            "message": "sukses",
            "data": data
        }, status=status.HTTP_200_OK)

