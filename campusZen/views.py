from rest_framework import viewsets
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import (
    Seuil, Question, Reponse, Questionnaire, Personne, Professionnel,
    Climat, Message, Ressource, Avis, Statut, ConsulteRessource, Recu,
    ConsultePro
)
from .serializers import (
    PersonneSerializer, ProfessionnelSerializer, ClimatSerializer,
    MessageSerializer, RessourceSerializer, AvisSerializer, StatutSerializer,
    ConsulteRessourceSerializer, RecuSerializer, ConsulteProSerializer,
    CustomTokenObtainPairSerializer, QuestionnaireSerializer,
    QuestionSerializer, ReponseSerializer, SeuilSerializer
)
from django.db import transaction
# from django.shortcuts import render
# from django.contrib.auth import authenticate


class PersonneViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer


class ProfessionnelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Professionnel.objects.all()
    serializer_class = ProfessionnelSerializer


class ClimatViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Climat.objects.all()
    serializer_class = ClimatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Message.objects.select_related('idClimat').all()
    serializer_class = MessageSerializer


class RessourceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer


class AvisViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Avis.objects.select_related('idPers').all()
    serializer_class = AvisSerializer


class StatutViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Statut.objects.select_related("personne", "climat").all()
    serializer_class = StatutSerializer


class ConsulteRessourceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = ConsulteRessource.objects.select_related('idR', 'idPers').all()
    serializer_class = ConsulteRessourceSerializer


class RecuViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Recu.objects.select_related("idPers", "idMessage").all()
    serializer_class = RecuSerializer


class ConsulteProViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = ConsultePro.objects.all()
    serializer_class = ConsulteProSerializer


class RegisterView(generics.CreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    # permission_classes = [IsAuthenticated] # Car sinon on ne peut pas s'inscrire
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Veuillez utiliser la méthode POST pour vous inscrire."}, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class MeView(APIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def get(self, request):
        serializer = PersonneSerializer(request.user)
        return Response(serializer.data)


class QuestionnairesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class ReponseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Reponse.objects.all()
    serializer_class = ReponseSerializer

    def get_queryset(self):
        queryset = Reponse.objects.all()

        question = self.request.query_params.get("question")

        if question:
            queryset = queryset.filter(question=question)

        return queryset


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()

        questionnaire_id = self.request.query_params.get("questionnaireId")

        if questionnaire_id:
            queryset = queryset.filter(questionnaireId=questionnaire_id)

        return queryset


class SeuilViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Seuil.objects.all()
    serializer_class = SeuilSerializer


class QuestionnaireDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class QuestionsListView(generics.ListCreateAPIView):
    """List or create questions for a specific questionnaire (nested endpoint).

    GET: list questions for questionnaire <pk>
    POST: create a question linked to questionnaire <pk>
    """
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        questionnaireId_id = self.kwargs['pk']
        return Question.objects.filter(questionnaireId_id=questionnaireId_id)

    def perform_create(self, serializer):
        questionnaireId_id = self.kwargs.get('pk')
        serializer.save(questionnaireId_id=questionnaireId_id)


class QuestionDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        questionnaireId_id = self.kwargs['pk']
        questionId_id = self.kwargs['question_pk']
        return Question.objects.filter(questionnaireId_id=questionnaireId_id, idQuestion=questionId_id)


class ReponseListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
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
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    serializer_class = ReponseSerializer

    def get_queryset(self):
        question_id = self.kwargs['question_pk']
        reponse_id = self.kwargs['reponse_pk']
        return Reponse.objects.filter(question_id=question_id, idReponse=reponse_id)


class SubmitQuestionnaireView(APIView):
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request, pk):
        data = request.data
        personne_id = data.get('idPers')
        reponses = data.get('reponses', [])
        questionnaire_id = pk
        print(personne_id)
        print(reponses)
        print(questionnaire_id)
        score_total = 0
        for reponse in reponses:
            question_id = reponse.get('idQuestion')
            reponse_id = reponse.get('idReponse')
            try:
                question = Question.objects.get(idQuestion=question_id)
                poids = question.poids
            except Question.DoesNotExist:
                poids = 1.0

            try:
                reponse_obj = Reponse.objects.get(idReponse=reponse_id, question_id=question_id)
                score = reponse_obj.score
            except Reponse.DoesNotExist:
                score = 1.0
            score_total += float(score) * float(poids)

        print(score_total)

        seuil = Seuil.objects.filter(questionnaire_id=questionnaire_id, minScore__lte=score_total, maxScore__gte=score_total).first()
        climat = None
        idClimat = None
        if seuil and seuil.climat:
            climat = seuil.climat
            idClimat = climat.idClimat

        if not Personne.objects.filter(idPers=personne_id).exists():
            return Response({"error": "Personne inexistante."}, status=400)

        if climat is None:
            return Response({"error": "Aucun climat trouvé pour ce score."}, status=400)

        Statut.objects.create(personne_id=personne_id, climat=climat, scoreTotal=score_total)

        return Response({
            "score_total": score_total,
            "idClimat": idClimat
        }, status=200)
