from django.test import TestCase
from campusZen.models import Climat, Message


class MessageModelTest(TestCase):
    """Tests pour le modèle Message"""

    def setUp(self):
        self.climat = Climat.objects.create(nomClimat="Stressé")
        self.message = Message.objects.create(
            message="Prenez le temps de respirer",
            idClimat=self.climat
        )

    def test_message_creation(self):
        """Test de création d'un message"""
        self.assertEqual(self.message.message, "Prenez le temps de respirer")
        self.assertEqual(self.message.idClimat, self.climat)

    def test_message_str(self):
        """Test de la méthode __str__ de Message"""
        expected = f"{self.message.idMessage} - {self.message.message} - {self.climat.nomClimat}"
        self.assertEqual(str(self.message), expected)
