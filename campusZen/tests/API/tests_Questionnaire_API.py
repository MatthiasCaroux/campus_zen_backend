from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Questionnaire, Personne


class QuestionnaireAPITest(APITestCase):
    """Tests de l'API Questionnaire"""

    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.client.force_authenticate(user=self.personne)
        self.questionnaire = Questionnaire.objects.create(
            nomQuestionnaire="Test Anxiété",
            descriptionQuestionnaire="Évaluation de l'anxiété"
        )
        self.url = reverse('questionnaire-list')

    def test_list_questionnaires(self):
        """Test de la liste des questionnaires"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_questionnaire(self):
        """Test de création d'un questionnaire"""
        data = {
            "nomQuestionnaire": "Test Stress",
            "descriptionQuestionnaire": "Évaluation du stress"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_questionnaire(self):
        """Test de récupération d'un questionnaire"""
        url = reverse('questionnaire-detail', args=[self.questionnaire.idQuestionnaire])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
