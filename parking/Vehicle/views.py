import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from vehicle.models import vehicle
from .serializer import vehicle_serializer     

# Create your views here.

class VehicleApiView(APIView):
    def get(self, request,*args, **kwargs):
        lista_vehiculos=vehicle.objects.all()
        serializer_vehiculos=vehicle_serializer(lista_vehiculos,many=True)
        return Response(serializer_vehiculos.data, status=status.HTTP_200_OK)
