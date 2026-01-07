from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Reponse, Question, Questionnaire

class ReponseAPITest(APITestCase):
    """Tests de l'API Reponse"""
    
    def setUp(self):
        self.client = APIClient()
        self.questionnaire = Questionnaire.objects.create(
            nomQuestionnaire="Test",
            descriptionQuestionnaire="Test"
        )
        self.question = Question.objects.create(
            intituleQuestion="Question test",
            questionnaireId=self.questionnaire
        )
        self.reponse = Reponse.objects.create(
            texte="Souvent",
            score=3,
            question=self.question
        )
        self.url = reverse('reponse-list')
    
    def test_list_reponses(self):
        """Test de la liste des réponses"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_filter_reponses_by_question(self):
        """Test du filtrage des réponses par question"""
        response = self.client.get(f"{self.url}?question={self.question.idQuestion}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_reponse(self):
        """Test de création d'une réponse"""
        data = {
            "texte": "Jamais",
            "score": 1,
            "question": self.question.idQuestion
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
