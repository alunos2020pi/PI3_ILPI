from betel.models import Hospede, Sinais_Vitais 
from rest_framework import serializers 


class HospedeSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Hospede 
        fields = ['nome_do_hospede',]

class Sinais_VitaisSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Sinais_Vitais 
        fields = ['hospede','data_hora', 'pa', 'pulso', 'resp', 'temp', 'sat', 'diures', 'evacuacao', 'responsavel'] 

