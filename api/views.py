from django.shortcuts import render

# Create your views here.

from betel.models import Hospede, Sinais_Vitais 
from rest_framework import viewsets 
from rest_framework import permissions 
from api.serializers import HospedeSerializer, Sinais_VitaisSerializer 

class HospedeViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar Sinais Vitais. 
    """ 
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer 
    permission_classes = [permissions.IsAuthenticated]
    
class Sinais_VitaisViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar Sinais Vitais. 
    """ 
    queryset = Sinais_Vitais.objects.all()
    serializer_class = Sinais_VitaisSerializer 
    permission_classes = [permissions.IsAuthenticated]