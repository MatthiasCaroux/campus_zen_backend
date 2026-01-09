from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import ConsultePro, Personne, Professionnel

class ConsulteProAPITest(APITestCase):
    """Tests de l'API ConsultePro"""
    
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
            adressePro="Test",
            lat=48.8566,
            long=2.3522
        )
        self.consulte = ConsultePro.objects.create(
            idPro=self.pro,
            idPers=self.personne
        )
        self.url = reverse('consultepro-list')
    
    def test_list_consulte_pro(self):
        """Test de la liste des consultations de professionnels"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
