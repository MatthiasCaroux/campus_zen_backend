from django.test import TestCase
from campusZen.models import Questionnaire

class QuestionnaireModelTest(TestCase):
    """Tests pour le modèle Questionnaire"""
    
    def setUp(self):
        self.questionnaire = Questionnaire.objects.create(
            nomQuestionnaire="Test Anxiété",
            descriptionQuestionnaire="Questionnaire pour évaluer l'anxiété"
        )
    
    def test_questionnaire_creation(self):
        """Test de création d'un questionnaire"""
        self.assertEqual(self.questionnaire.nomQuestionnaire, "Test Anxiété")
        self.assertEqual(self.questionnaire.descriptionQuestionnaire, "Questionnaire pour évaluer l'anxiété")
    
    def test_questionnaire_str(self):
        """Test de la méthode __str__ de Questionnaire"""
        expected = f"{self.questionnaire.idQuestionnaire} - {self.questionnaire.nomQuestionnaire}"
        self.assertEqual(str(self.questionnaire), expected)

