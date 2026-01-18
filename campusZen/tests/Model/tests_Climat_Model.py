from django.test import TestCase
from campusZen.models import Climat


class ClimatModelTest(TestCase):
    """Tests pour le modèle Climat"""

    def setUp(self):
        self.climat = Climat.objects.create(nomClimat="Anxieux")

    def test_climat_creation(self):
        """Test de création d'un climat"""
        self.assertEqual(self.climat.nomClimat, "Anxieux")

    def test_climat_str(self):
        """Test de la méthode __str__ de Climat"""
        self.assertEqual(str(self.climat), "Anxieux")
