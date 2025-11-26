from datetime import timedelta, datetime
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import *

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
    username_field = 'emailPers'

    emailPers = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        emailPers = attrs.get('emailPers')
        passwordPers = attrs.get('password')

        if emailPers is None or passwordPers is None:
            raise serializers.ValidationError({
                'detail': 'Les champs emailPers et passwordPers sont requis.'
            })

        # Authentification de l'utilisateur
        user = authenticate(
            request=self.context.get('request'),
            emailPers=emailPers,
            password=passwordPers
        )

        if user is None:
            raise serializers.ValidationError({'detail': 'Identifiants invalides.'})

        # Appel du parent pour générer les tokens
        data = super().validate({
            self.username_field: emailPers,
            'password': passwordPers
        })

        # Ajout d'informations supplémentaires dans la réponse
        data['idPers'] = user.idPers
        data['role'] = user.role
        data['emailPers'] = user.emailPers
        data['lastConnection'] = str(user.lastConnection)
        accessLifetime = self.get_token(user).access_token.lifetime
        data['endAccess'] = (accessLifetime + datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        refreshLifetime = self.get_token(user).lifetime
        data['endRefresh'] = (refreshLifetime + datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['idPers'] = user.idPers
        token['role'] = user.role
        token['emailPers'] = user.emailPers
        token['lastConnection'] = str(user.lastConnection)
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

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = '__all__'

class SeuilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seuil
        fields = '__all__'

