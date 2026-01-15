from django.test import TestCase
from campusZen.models import Seuil, Questionnaire, Climat


class SeuilModelTest(TestCase):
    """Tests pour le modèle Seuil"""

    def setUp(self):
        self.questionnaire = Questionnaire.objects.create(
            nomQuestionnaire="Test",
            descriptionQuestionnaire="Test"
        )
        self.climat = Climat.objects.create(nomClimat="Serein")
        self.seuil = Seuil.objects.create(
            questionnaire=self.questionnaire,
            climat=self.climat,
            minScore=0,
            maxScore=10,
            description="Niveau faible"
        )

    def test_seuil_creation(self):
        """Test de création d'un seuil"""
        self.assertEqual(self.seuil.minScore, 0)
        self.assertEqual(self.seuil.maxScore, 10)
        self.assertEqual(self.seuil.description, "Niveau faible")
        self.assertEqual(self.seuil.questionnaire, self.questionnaire)
        self.assertEqual(self.seuil.climat, self.climat)

    def test_seuil_str(self):
        """Test de la méthode __str__ de Seuil"""
        expected = f"{self.seuil.minScore}-{self.seuil.maxScore} : {self.seuil.description}"
        self.assertEqual(str(self.seuil), expected)
