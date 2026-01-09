from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Avis, Personne

class AvisAPITest(APITestCase):
    """Tests de l'API Avis"""
    
    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.client.force_authenticate(user=self.personne)
        self.avis = Avis.objects.create(
            nbEtoile=5,
            messageAvis="Excellent",
            idPers=self.personne
        )
        self.url = reverse('avis-list')
    
    def test_list_avis(self):
        """Test de la liste des avis"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_create_avis(self):
        """Test de création d'un avis"""
        data = {
            "nbEtoile": 4,
            "messageAvis": "Très bien",
            "idPers": self.personne.idPers
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
