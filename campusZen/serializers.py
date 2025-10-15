from rest_framework import serializers
from .models import Personne, Professionnel, Climat, Message, Ressource, Avis, Question, Statut, ConsulteRessource, Recu, ConsultePro
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PersonneSerializer(serializers.ModelSerializer):
    passwordPers = serializers.CharField(write_only=True)

    class Meta:
        model = Personne
        fields = ("idPers", "emailPers", "passwordPers", "role", "lastConnection")

    def create(self, validated_data):
        password = validated_data.pop("passwordPers", None)
        personne = Personne(**validated_data)
        if password:
            personne.set_password(password)
        personne.save()
        return personne

    @property
    def id(self):  # simple alias pour JWT
        return self.idPers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['idPers'] = user.idPers
        token['role'] = user.role
        token['emailPers'] = user.emailPers
        return token

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
    idPers = PersonneSerializer()

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


class ConsulteRessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsulteRessource
        fields = '__all__'


class ConsulteProSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultePro
        fields = '__all__'


class StatutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statut
        fields = '__all__'


class RecuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recu
        fields = '__all__'
