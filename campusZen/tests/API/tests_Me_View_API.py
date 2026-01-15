from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Personne


class MeViewTest(APITestCase):
    """Tests de la vue Me"""

    def setUp(self):
        self.client = APIClient()
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.url = reverse('me')

    def test_me_view(self):
        """Test de la vue Me (profil utilisateur)"""
        # Note: Cette vue nécessite d'être authentifié normalement
        # mais les permissions sont AllowAny pour l'instant
        self.client.force_authenticate(user=self.personne)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# ============================================================================
# Tests des Serializers
# ============================================================================
