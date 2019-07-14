from rest_framework import serializers
from bee.models import *

class ApicultorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apicultor
        fields = '__all__'

class ApiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apiario
        fields = '__all__'

class CaixaRacionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaixaRacional
        fields = '__all__'

class PerdaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perda
        fields = '__all__'
        