from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from campusZen.models import Personne, Questionnaire, Question, Reponse, Seuil, Climat, Statut

class SubmitQuestionnaireAPITest(APITestCase):
    """Tests de l'API de soumission de questionnaire"""
    
    def setUp(self):
        self.client = APIClient()
        
        # Créer une personne
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        
        # Créer un questionnaire
        self.questionnaire = Questionnaire.objects.create(
            nomQuestionnaire="Test Anxiété",
            descriptionQuestionnaire="Test"
        )
        
        # Créer des questions
        self.question1 = Question.objects.create(
            intituleQuestion="Question 1",
            poids=1.0,
            questionnaireId=self.questionnaire
        )
        self.question2 = Question.objects.create(
            intituleQuestion="Question 2",
            poids=2.0,
            questionnaireId=self.questionnaire
        )
        
        # Créer des réponses
        self.reponse1 = Reponse.objects.create(
            texte="Jamais",
            score=1,
            question=self.question1
        )
        self.reponse2 = Reponse.objects.create(
            texte="Souvent",
            score=3,
            question=self.question2
        )
        
        # Créer un climat et des seuils
        self.climat = Climat.objects.create(nomClimat="Anxieux")
        self.seuil = Seuil.objects.create(
            questionnaire=self.questionnaire,
            climat=self.climat,
            minScore=0,
            maxScore=10,
            description="Anxiété modérée"
        )
        
        self.url = reverse('submit-questionnaire', args=[self.questionnaire.idQuestionnaire])
    
    def test_submit_questionnaire_success(self):
        """Test de soumission réussie d'un questionnaire"""
        data = {
            "idPers": self.personne.idPers,
            "reponses": [
                {
                    "idQuestion": self.question1.idQuestion,
                    "idReponse": self.reponse1.idReponse
                },
                {
                    "idQuestion": self.question2.idQuestion,
                    "idReponse": self.reponse2.idReponse
                }
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("score_total", response.data)
        self.assertIn("idClimat", response.data)
        
        # Vérifier qu'un statut a été créé
        self.assertTrue(Statut.objects.filter(personne=self.personne).exists())
    
    def test_submit_questionnaire_nonexistent_person(self):
        """Test de soumission avec une personne inexistante"""
        data = {
            "idPers": 99999,
            "reponses": []
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
    
    def test_submit_questionnaire_no_matching_seuil(self):
        """Test de soumission sans seuil correspondant au score"""
        # Supprimer le seuil existant
        Seuil.objects.all().delete()
        
        data = {
            "idPers": self.personne.idPers,
            "reponses": [
                {
                    "idQuestion": self.question1.idQuestion,
                    "idReponse": self.reponse1.idReponse
                }
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)
