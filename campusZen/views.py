from rest_framework import viewsets
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Personne, Professionnel, Climat, Message, Ressource, Avis, Question, Statut, ConsulteRessource, Recu, ConsultePro
from .serializers import PersonneSerializer, ProfessionnelSerializer, ClimatSerializer, MessageSerializer, RessourceSerializer, AvisSerializer, QuestionSerializer, StatutSerializer, ConsulteRessourceSerializer, RecuSerializer, ConsulteProSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
# from django.shortcuts import render
# from django.contrib.auth import authenticate


class PersonneViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer


class ProfessionnelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Professionnel.objects.all()
    serializer_class = ProfessionnelSerializer


class ClimatViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Climat.objects.all()
    serializer_class = ClimatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.select_related('idClimat').all()
    serializer_class = MessageSerializer


class RessourceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer


class AvisViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Avis.objects.select_related('idPers').all()
    serializer_class = AvisSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class StatutViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Statut.objects.select_related("idPers", "idClimat").all()
    serializer_class = StatutSerializer


class ConsulteRessourceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ConsulteRessource.objects.select_related('idR', 'idPers').all()
    serializer_class = ConsulteRessourceSerializer


class RecuViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Recu.objects.select_related("idPers", "idMessage").all()
    serializer_class = RecuSerializer


class ConsulteProViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ConsultePro.objects.all()
    serializer_class = ConsulteProSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"message": "Veuillez utiliser la méthode POST pour vous inscrire."}, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
