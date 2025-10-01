from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework import generics, permissions, status
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

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


class RegisterView(generics.CreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"message": "Veuillez utiliser la méthode POST pour vous inscrire."}, status=status.HTTP_200_OK)
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonneSerializer
    def get_queryset(self):
        return Personne.objects.all()

    def get(self, request):
        return Response({"message": "Veuillez utiliser la méthode POST pour vous connecter."}, status=status.HTTP_200_OK)

    def post(self, request):
        email = request.data.get("emailPers")
        password = request.data.get("passwordPers")

        try:
            personne = Personne.objects.get(emailPers=email)
        except Personne.DoesNotExist:
            return Response({"error": "Utilisateur introuvable"}, status=status.HTTP_404_NOT_FOUND)

        if not personne.check_password(password):
            return Response({"error": "Mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        # Génération JWT
        refresh = RefreshToken.for_user(personne)

        return Response({
            "message": "Vous êtes bien connecté ✅",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "idPers": personne.idPers,
            "mail": personne.emailPers,
        }, status=status.HTTP_200_OK)
