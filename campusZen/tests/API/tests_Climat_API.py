from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Climat

class ClimatAPITest(APITestCase):
    """Tests de l'API Climat"""
    
    def setUp(self):
        self.client = APIClient()
        self.climat = Climat.objects.create(nomClimat="Anxieux")
        self.url = reverse('climat-list')
    
    def test_list_climats(self):
        """Test de la liste des climats"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_create_climat(self):
        """Test de création d'un climat"""
        data = {"nomClimat": "Serein"}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Climat.objects.filter(nomClimat="Serein").exists())
