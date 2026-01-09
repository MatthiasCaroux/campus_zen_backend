from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Professionnel, Personne

class ProfessionnelAPITest(APITestCase):
    """Tests de l'API Professionnel"""
    
    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.client.force_authenticate(user=self.personne)
        self.pro = Professionnel.objects.create(
            nomPro="Dupont",
            prenomPro="Jean",
            fonctionPro="Psychologue",
            emailPro="pro@example.com",
            telephonePro="0123456789",
            adressePro="1 rue de la paix",
            lat=48.8566,
            long=2.3522
        )
        self.url = reverse('professionnel-list')
    
    def test_list_professionnels(self):
        """Test de la liste des professionnels"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_retrieve_professionnel(self):
        """Test de récupération d'un professionnel"""
        url = reverse('professionnel-detail', args=[self.pro.idPro])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['emailPro'], "pro@example.com")
    
    def test_create_professionnel(self):
        """Test de création d'un professionnel"""
        data = {
            "nomPro": "Martin",
            "prenomPro": "Paul",
            "fonctionPro": "Médecin",
            "emailPro": "martin@example.com",
            "telephonePro": "0987654321",
            "adressePro": "2 avenue test",
            "lat": 45.764,
            "long": 4.8357
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Professionnel.objects.filter(emailPro="martin@example.com").exists())
