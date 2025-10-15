from rest_framework import serializers
from .models import (
    Personne,
    Professionnel,
    Climat,
    Message,
    Ressource,
    Avis,
    Question,
    Statut,
    ConsulteRessource,
    Recu,
    ConsultePro,
    Questionnaire,
    Reponse,
    Seuil,
)


class PersonneSerializer(serializers.ModelSerializer):
    passwordPers = serializers.CharField(write_only=True)

    class Meta:
        model = Personne
        fields = ("idPers", "emailPers", "passwordPers", "lastConnection")

    def create(self, validated_data):
        password = validated_data.pop("passwordPers")
        personne = Personne(**validated_data)
        personne.set_password(password)  # hash le mdp
        personne.save()
        return personne


class ClimatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    idClimat = ClimatSerializer(read_only=True)
    idClimat_id = serializers.PrimaryKeyRelatedField(
        queryset=Climat.objects.all(), source="idClimat", write_only=True)

    class Meta:
        model = Message
        fields = ["idMessage", "message", "idClimat", "idClimat_id"]


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


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = '__all__'


class SeuilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seuil
        fields = '__all__'