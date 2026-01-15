from django.test import TestCase
from campusZen.models import ConsulteRessource, Personne, Ressource


class ConsulteRessourceModelTest(TestCase):
    """Tests pour le modèle ConsulteRessource"""

    def setUp(self):
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
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

    def test_consulte_ressource_creation(self):
        """Test de création d'une consultation de ressource"""
        self.assertEqual(self.consulte.idR, self.ressource)
        self.assertEqual(self.consulte.idPers, self.personne)
