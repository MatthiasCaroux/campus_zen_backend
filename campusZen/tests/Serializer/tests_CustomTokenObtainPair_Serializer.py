from django.test import TestCase
from campusZen.models import Personne
from campusZen.serializers import CustomTokenObtainPairSerializer
from rest_framework import serializers


class CustomTokenObtainPairSerializerTest(TestCase):
    """Tests du serializer CustomTokenObtainPair"""

    def setUp(self):
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass123",
            role="étudiant"
        )

    def test_validate_correct_credentials(self):
        """Test de validation avec des identifiants corrects"""
        serializer = CustomTokenObtainPairSerializer(data={
            'emailPers': 'test@example.com',
            'password': 'testpass123'
        })
        self.assertTrue(serializer.is_valid())
        validated_data = serializer.validated_data

        self.assertIn('access', validated_data)
        self.assertIn('refresh', validated_data)
        self.assertEqual(validated_data['idPers'], self.personne.idPers)
        self.assertEqual(validated_data['role'], "étudiant")
        self.assertIn('endAccess', validated_data)
        self.assertIn('endRefresh', validated_data)

    def test_validate_wrong_credentials(self):
        """Test de validation avec des identifiants incorrects"""
        serializer = CustomTokenObtainPairSerializer(data={
            'emailPers': 'test@example.com',
            'password': 'wrongpassword'
        })
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
