from django.test import TestCase
from campusZen.models import Personne
from campusZen.serializers import PersonneSerializer


class PersonneSerializerTest(TestCase):
    """Tests du serializer Personne"""

    def test_serialize_personne(self):
        """Test de sérialisation d'une personne"""
        personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass",
            role="étudiant"
        )
        serializer = PersonneSerializer(personne)
        data = serializer.data

        self.assertEqual(data['emailPers'], "test@example.com")
        self.assertEqual(data['role'], "étudiant")
        self.assertNotIn('passwordPers', data)  # Le mot de passe ne doit pas être sérialisé

    def test_deserialize_personne(self):
        """Test de désérialisation d'une personne"""
        data = {
            "emailPers": "new@example.com",
            "passwordPers": "newpass123",
            "role": "admin"
        }
        serializer = PersonneSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        personne = serializer.save()

        self.assertEqual(personne.emailPers, "new@example.com")
        self.assertTrue(personne.check_password("newpass123"))
        self.assertEqual(personne.role, "admin")
