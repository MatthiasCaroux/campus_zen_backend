from django.test import TestCase
from campusZen.models import Avis, Personne


class AvisModelTest(TestCase):
    """Tests pour le modèle Avis"""

    def setUp(self):
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.avis = Avis.objects.create(
            nbEtoile=5,
            messageAvis="Excellent service",
            idPers=self.personne
        )

    def test_avis_creation(self):
        """Test de création d'un avis"""
        self.assertEqual(self.avis.nbEtoile, 5)
        self.assertEqual(self.avis.messageAvis, "Excellent service")
        self.assertEqual(self.avis.idPers, self.personne)
        self.assertIsNotNone(self.avis.dateAvis)

    def test_avis_str(self):
        """Test de la méthode __str__ de Avis"""
        expected = f"{self.avis.idAvis} - {self.avis.nbEtoile} - {self.avis.messageAvis} - {self.avis.dateAvis} - {self.personne.emailPers} ({self.personne.role})"
        self.assertEqual(str(self.avis), expected)
