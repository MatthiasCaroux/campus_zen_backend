from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Question, Questionnaire, Personne


class QuestionAPITest(APITestCase):
    """Tests de l'API Question"""

    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.client.force_authenticate(user=self.personne)
        self.questionnaire = Questionnaire.objects.create(
            nomQuestionnaire="Test",
            descriptionQuestionnaire="Test"
        )
        self.question = Question.objects.create(
            intituleQuestion="Êtes-vous stressé ?",
            poids=1.0,
            questionnaireId=self.questionnaire
        )
        self.url = reverse('question-list')

    def test_list_questions(self):
        """Test de la liste des questions"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_filter_questions_by_questionnaire(self):
        """Test du filtrage des questions par questionnaire"""
        response = self.client.get(f"{self.url}?questionnaireId={self.questionnaire.idQuestionnaire}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_question(self):
        """Test de création d'une question"""
        data = {
            "intituleQuestion": "Nouvelle question ?",
            "poids": 2.0,
            "questionnaireId": self.questionnaire.idQuestionnaire
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
