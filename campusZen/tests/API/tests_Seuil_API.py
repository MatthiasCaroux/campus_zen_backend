from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Seuil, Questionnaire, Climat, Personne

class SeuilAPITest(APITestCase):
    """Tests de l'API Seuil"""
    
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
        self.climat = Climat.objects.create(nomClimat="Serein")
        self.seuil = Seuil.objects.create(
            questionnaire=self.questionnaire,
            climat=self.climat,
            minScore=0,
            maxScore=10,
            description="Niveau faible"
        )
        self.url = reverse('seuil-list')
    
    def test_list_seuils(self):
        """Test de la liste des seuils"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_create_seuil(self):
        """Test de création d'un seuil"""
        data = {
            "questionnaire": self.questionnaire.idQuestionnaire,
            "climat": self.climat.idClimat,
            "minScore": 11,
            "maxScore": 20,
            "description": "Niveau moyen"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
