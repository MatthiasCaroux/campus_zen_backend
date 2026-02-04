from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Recu, Personne, Message, Climat


class RecuAPITest(APITestCase):
    """Tests de l'API Recu"""

    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.client.force_authenticate(user=self.personne)
        self.climat = Climat.objects.create(nomClimat="Stressé")
        self.message = Message.objects.create(
            message="Test",
            idClimat=self.climat
        )
        self.recu = Recu.objects.create(
            idPers=self.personne,
            idMessage=self.message
        )
        self.url = reverse('recu-list')

    def test_list_recus(self):
        """Test de la liste des messages reçus"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
