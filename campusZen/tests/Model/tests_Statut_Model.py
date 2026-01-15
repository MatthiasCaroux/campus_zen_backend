from django.test import TestCase
from campusZen.models import Statut, Personne, Climat


class StatutModelTest(TestCase):
    """Tests pour le modèle Statut"""

    def setUp(self):
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.climat = Climat.objects.create(nomClimat="Anxieux")
        self.statut = Statut.objects.create(
            personne=self.personne,
            climat=self.climat,
            scoreTotal=15.5
        )

    def test_statut_creation(self):
        """Test de création d'un statut"""
        self.assertEqual(self.statut.personne, self.personne)
        self.assertEqual(self.statut.climat, self.climat)
        self.assertEqual(self.statut.scoreTotal, 15.5)
        self.assertIsNotNone(self.statut.dateStatut)

    def test_statut_str(self):
        """Test de la méthode __str__ de Statut"""
        expected = f"{self.personne} - {self.climat} - {self.statut.scoreTotal} - {self.statut.dateStatut}"
        self.assertEqual(str(self.statut), expected)
