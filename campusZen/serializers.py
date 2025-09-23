from rest_framework import serializers
from .models import *

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = '__all__'

class ClimatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climat
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ressource
        fields = '__all__'

class AvisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avis
        fields = '__all__'

class ProfessionnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professionnel
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ConsulteProSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultePro
        fields = '__all__'

class ConsulteRessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsulteRessource
        fields = '__all__'

class ConsulteProSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultePro
        fields = '__all__'

class ConsulteProSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultePro
        fields = '__all__'
