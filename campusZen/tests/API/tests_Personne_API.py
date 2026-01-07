from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Personne


class PersonneAPITest(APITestCase):
    """Tests de l'API Personne"""
    
    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass123"
        )
        self.url = reverse('personne-list')
    
    def test_list_personnes(self):
        """Test de la liste des personnes"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_retrieve_personne(self):
        """Test de récupération d'une personne"""
        url = reverse('personne-detail', args=[self.personne.idPers])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['emailPers'], "test@example.com")
    
    def test_create_personne(self):
        """Test de création d'une personne"""
        data = {
            "emailPers": "new@example.com",
            "passwordPers": "newpass123",
            "role": "étudiant"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Personne.objects.filter(emailPers="new@example.com").exists())
    
    def test_update_personne(self):
        """Test de mise à jour d'une personne"""
        url = reverse('personne-detail', args=[self.personne.idPers])
        data = {
            "emailPers": "updated@example.com",
            "passwordPers": "newpass",
            "role": "admin"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_delete_personne(self):
        """Test de suppression d'une personne"""
        url = reverse('personne-detail', args=[self.personne.idPers])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Personne.objects.filter(idPers=self.personne.idPers).exists())
        
        
