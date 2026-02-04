from django.test import TestCase
from campusZen.models import Reponse, Question, Questionnaire


class ReponseModelTest(TestCase):
    """Tests pour le modèle Reponse"""

    def setUp(self):
        self.questionnaire = Questionnaire.objects.create(
            nomQuestionnaire="Test",
            descriptionQuestionnaire="Test"
        )
        self.question = Question.objects.create(
            intituleQuestion="Question test",
            questionnaireId=self.questionnaire
        )
        self.reponse = Reponse.objects.create(
            texte="Souvent",
            score=3,
            question=self.question
        )

    def test_reponse_creation(self):
        """Test de création d'une réponse"""
        self.assertEqual(self.reponse.texte, "Souvent")
        self.assertEqual(self.reponse.score, 3)
        self.assertEqual(self.reponse.question, self.question)

    def test_reponse_str(self):
        """Test de la méthode __str__ de Reponse"""
        expected = f"{self.reponse.idReponse} - {self.reponse.texte} ({self.reponse.score})"
        self.assertEqual(str(self.reponse), expected)
