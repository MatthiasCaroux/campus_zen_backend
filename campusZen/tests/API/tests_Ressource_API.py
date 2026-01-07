from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Ressource

class RessourceAPITest(APITestCase):
    """Tests de l'API Ressource"""
    
    def setUp(self):
        self.client = APIClient()
        self.ressource = Ressource.objects.create(
            typeR="article",
            titreR="Gestion du stress",
            descriptionR="Article sur la gestion du stress",
            lienR="https://example.com/stress"
        )
        self.url = reverse('ressource-list')
    
    def test_list_ressources(self):
        """Test de la liste des ressources"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_create_ressource(self):
        """Test de création d'une ressource"""
        data = {
            "typeR": "video",
            "titreR": "Vidéo relaxation",
            "descriptionR": "Une vidéo de relaxation",
            "lienR": "https://example.com/relax"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_retrieve_ressource(self):
        """Test de récupération d'une ressource"""
        url = reverse('ressource-detail', args=[self.ressource.idR])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titreR'], "Gestion du stress")
