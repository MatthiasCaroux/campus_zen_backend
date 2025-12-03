from rest_framework import viewsets
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *
# from django.shortcuts import render
# from django.contrib.auth import authenticate


class PersonneViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer


class ProfessionnelViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Professionnel.objects.all()
    serializer_class = ProfessionnelSerializer


class ClimatViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Climat.objects.all()
    serializer_class = ClimatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Message.objects.select_related('idClimat').all()
    serializer_class = MessageSerializer


class RessourceViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer


class AvisViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Avis.objects.select_related('idPers').all()
    serializer_class = AvisSerializer



class StatutViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Statut.objects.select_related("personne", "climat").all()
    serializer_class = StatutSerializer


class ConsulteRessourceViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = ConsulteRessource.objects.select_related('idR', 'idPers').all()
    serializer_class = ConsulteRessourceSerializer


class RecuViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    queryset = Recu.objects.select_related("idPers", "idMessage").all()
    serializer_class = RecuSerializer


class ConsulteProViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
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


class MeView(APIView):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def get(self, request):
        serializer = PersonneSerializer(request.user)
        return Response(serializer.data)

class QuestionnairesViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

class ReponseViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Reponse.objects.all()
    serializer_class = ReponseSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class SeuilViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Seuil.objects.all()
    serializer_class = SeuilSerializer

class QuestionnaireDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

class QuestionsListView(generics.ListCreateAPIView):
    """List or create questions for a specific questionnaire (nested endpoint).

    GET: list questions for questionnaire <pk>
    POST: create a question linked to questionnaire <pk>
    """
    permission_classes = [AllowAny]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        questionnaireId_id = self.kwargs['pk']
        return Question.objects.filter(questionnaireId_id=questionnaireId_id)

    def perform_create(self, serializer):
        questionnaireId_id = self.kwargs.get('pk')
        serializer.save(questionnaireId_id=questionnaireId_id)

class QuestionDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        questionnaireId_id = self.kwargs['pk']
        questionId_id = self.kwargs['question_pk']
        return Question.objects.filter(questionnaireId_id=questionnaireId_id, idQuestion=questionId_id)

class ReponseListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReponseSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_pk']
        return Reponse.objects.filter(question_id=question_id)

    def perform_create(self, serializer):
        question_id = self.kwargs.get('question_pk')
        if question_id is None:
            raise ValidationError({"detail": "Paramètre question_pk manquant dans l'URL."})
        serializer.save(question_id=question_id)


class ReponseDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ReponseSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_pk']
        reponse_id = self.kwargs['reponse_pk']
        return Reponse.objects.filter(question_id=question_id, idReponse=reponse_id)