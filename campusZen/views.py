from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class PersonneViewSet(viewsets.ModelViewSet):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer

class ProfessionnelViewSet(viewsets.ModelViewSet):
    queryset = Professionnel.objects.all()
    serializer_class = ProfessionnelSerializer

class ClimatViewSet(viewsets.ModelViewSet):
    queryset = Climat.objects.all()
    serializer_class = ClimatSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.select_related('idClimat').all()
    serializer_class = MessageSerializer

class RessourceViewSet(viewsets.ModelViewSet):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer

class AvisViewSet(viewsets.ModelViewSet):
    queryset = Avis.objects.select_related('idPers').all()
    serializer_class = AvisSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class StatutViewSet(viewsets.ModelViewSet):
    queryset = Statut.objects.select_related("idPers", "idClimat").all()
    serializer_class = StatutSerializer

class ConsulteRessourceViewSet(viewsets.ModelViewSet):
    queryset = ConsulteRessource.objects.select_related('idR', 'idPers').all()
    serializer_class = ConsulteRessourceSerializer

class RecuViewSet(viewsets.ModelViewSet):
    queryset = Recu.objects.select_related("idPers", "idMessage").all()
    serializer_class = RecuSerializer

class ConsulteProViewSet(viewsets.ModelViewSet):
    queryset = ConsultePro.objects.all()
    serializer_class = ConsulteProSerializer


