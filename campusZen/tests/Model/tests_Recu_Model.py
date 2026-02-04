from django.test import TestCase
from campusZen.models import Recu, Personne, Message, Climat


class RecuModelTest(TestCase):
    """Tests pour le modèle Recu"""

    def setUp(self):
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.climat = Climat.objects.create(nomClimat="Stressé")
        self.message = Message.objects.create(
            message="Test message",
            idClimat=self.climat
        )
        self.recu = Recu.objects.create(
            idPers=self.personne,
            idMessage=self.message
        )

    def test_recu_creation(self):
        """Test de création d'un message reçu"""
        self.assertEqual(self.recu.idPers, self.personne)
        self.assertEqual(self.recu.idMessage, self.message)
        self.assertIsNotNone(self.recu.dateMessage)
