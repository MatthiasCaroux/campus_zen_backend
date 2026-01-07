from django.test import TestCase
from campusZen.models import Question, Questionnaire

class QuestionModelTest(TestCase):
    """Tests pour le modèle Question"""
    
    def setUp(self):
        self.questionnaire = Questionnaire.objects.create(
            nomQuestionnaire="Test",
            descriptionQuestionnaire="Description test"
        )
        self.question = Question.objects.create(
            intituleQuestion="Vous sentez-vous stressé ?",
            poids=1.5,
            questionnaireId=self.questionnaire
        )
    
    def test_question_creation(self):
        """Test de création d'une question"""
        self.assertEqual(self.question.intituleQuestion, "Vous sentez-vous stressé ?")
        self.assertEqual(self.question.poids, 1.5)
        self.assertEqual(self.question.questionnaireId, self.questionnaire)
    
    def test_question_str(self):
        """Test de la méthode __str__ de Question"""
        expected = f"{self.question.idQuestion} - {self.question.intituleQuestion} - {self.question.poids} - {self.questionnaire.idQuestionnaire} - {self.questionnaire.nomQuestionnaire}"
        self.assertEqual(str(self.question), expected)
