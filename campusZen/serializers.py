from rest_framework import serializers
from .models import *

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

    @property
    def id(self):  # simple alias pour JWT
        return self.idPers

class ClimatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Climat
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    idClimat = ClimatSerializer(read_only=True)
    idClimat_id = serializers.PrimaryKeyRelatedField(
        queryset=Climat.objects.all(), source="idClimat", write_only=True
    )
    class Meta:
        model = Message
        # fields = '__all__'
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

class ConsulteProSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultePro
        fields = '__all__'

class ConsulteRessourceSerializer(serializers.ModelSerializer):
    # idR = RessourceSerializer()
    # idPers = PersonneSerializer()
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

