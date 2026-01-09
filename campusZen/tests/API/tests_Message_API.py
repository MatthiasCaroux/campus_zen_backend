from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Message, Climat, Personne

class MessageAPITest(APITestCase):
    """Tests de l'API Message"""
    
    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.client.force_authenticate(user=self.personne)
        self.climat = Climat.objects.create(nomClimat="Stressé")
        self.message = Message.objects.create(
            message="Prenez le temps de respirer",
            idClimat=self.climat
        )
        self.url = reverse('message-list')
    
    def test_list_messages(self):
        """Test de la liste des messages"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_create_message(self):
        """Test de création d'un message"""
        data = {
            "message": "Nouveau message",
            "idClimat": self.climat.idClimat
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
