from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Statut, Personne, Climat

class StatutAPITest(APITestCase):
    """Tests de l'API Statut"""
    
    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.client.force_authenticate(user=self.personne)
        self.climat = Climat.objects.create(nomClimat="Anxieux")
        self.statut = Statut.objects.create(
            personne=self.personne,
            climat=self.climat,
            scoreTotal=15.5
        )
        self.url = reverse('statut-list')
    
    def test_list_statuts(self):
        """Test de la liste des statuts"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_create_statut(self):
        """Test de création d'un statut"""
        data = {
            "personne": self.personne.idPers,
            "climat": self.climat.idClimat,
            "scoreTotal": 20.0
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
