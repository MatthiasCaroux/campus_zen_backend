from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import ConsulteRessource, Personne, Ressource


class ConsulteRessourceAPITest(APITestCase):
    """Tests de l'API ConsulteRessource"""

    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.client.force_authenticate(user=self.personne)
        self.ressource = Ressource.objects.create(
            typeR="article",
            titreR="Test",
            descriptionR="Test",
            lienR="https://example.com"
        )
        self.consulte = ConsulteRessource.objects.create(
            idR=self.ressource,
            idPers=self.personne
        )
        self.url = reverse('consulteressource-list')

    def test_list_consulte_ressources(self):
        """Test de la liste des consultations de ressources"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
