from django.test import TestCase
from campusZen.models import Professionnel


class ProfessionnelModelTest(TestCase):
    """Tests pour le modèle Professionnel"""
    
    def setUp(self):
        self.pro = Professionnel.objects.create(
            nomPro="Dupont",
            prenomPro="Jean",
            fonctionPro="Psychologue",
            emailPro="dupont@example.com",
            telephonePro="0123456789",
            adressePro="1 rue de la paix, Paris",
            lat=48.8566,
            long=2.3522
        )
    
    def test_professionnel_creation(self):
        """Test de création d'un professionnel"""
        self.assertEqual(self.pro.nomPro, "Dupont")
        self.assertEqual(self.pro.prenomPro, "Jean")
        self.assertEqual(self.pro.fonctionPro, "Psychologue")
        self.assertEqual(self.pro.emailPro, "dupont@example.com")
        self.assertEqual(self.pro.lat, 48.8566)
        self.assertEqual(self.pro.long, 2.3522)
    
    def test_professionnel_str(self):
        """Test de la méthode __str__ de Professionnel"""
        expected = f"{self.pro.nomPro} - {self.pro.prenomPro} - {self.pro.emailPro} - {self.pro.fonctionPro}"
        self.assertEqual(str(self.pro), expected)
    
    def test_professionnel_unique_email(self):
        """Test de l'unicité de l'email du professionnel"""
        with self.assertRaises(Exception):
            Professionnel.objects.create(
                nomPro="Martin",
                prenomPro="Paul",
                fonctionPro="Médecin",
                emailPro="dupont@example.com",  # Email déjà utilisé
                telephonePro="0987654321",
                adressePro="2 rue de la liberté",
                lat=45.764,
                long=4.8357
            )
