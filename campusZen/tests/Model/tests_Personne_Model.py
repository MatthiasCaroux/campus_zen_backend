from django.test import TestCase
from campusZen.models import Personne


class PersonneModelTest(TestCase):
    """Tests pour le modèle Personne"""
    
    def setUp(self):
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass123",
            role="étudiant"
        )
    
    def test_personne_creation(self):
        """Test de création d'une personne"""
        self.assertEqual(self.personne.emailPers, "test@example.com")
        self.assertEqual(self.personne.role, "étudiant")
        self.assertTrue(self.personne.check_password("testpass123"))
        self.assertTrue(self.personne.is_active)
        self.assertFalse(self.personne.is_staff)
    
    def test_personne_str(self):
        """Test de la méthode __str__ de Personne"""
        expected = f"{self.personne.emailPers} ({self.personne.role})"
        self.assertEqual(str(self.personne), expected)
    
    def test_create_superuser(self):
        """Test de création d'un superutilisateur"""
        admin = Personne.objects.create_superuser(
            emailPers="admin@example.com",
            passwordPers="adminpass123"
        )
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertEqual(admin.role, "admin")
    
    def test_personne_without_email(self):
        """Test de création d'une personne sans email"""
        with self.assertRaises(ValueError):
            Personne.objects.create_user(emailPers="", passwordPers="test")
    
    def test_personne_id_property(self):
        """Test de la propriété id"""
        self.assertEqual(self.personne.id, self.personne.idPers)
