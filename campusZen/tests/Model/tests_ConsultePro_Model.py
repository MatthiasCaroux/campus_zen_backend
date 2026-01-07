from django.test import TestCase
from campusZen.models import ConsultePro, Personne, Professionnel


class ConsulteProModelTest(TestCase):
    """Tests pour le modèle ConsultePro"""
    
    def setUp(self):
        self.personne = Personne.objects.create_user(
            emailPers="test@example.com",
            passwordPers="testpass"
        )
        self.pro = Professionnel.objects.create(
            nomPro="Dupont",
            prenomPro="Jean",
            fonctionPro="Psychologue",
            emailPro="pro@example.com",
            telephonePro="0123456789",
            adressePro="Test",
            lat=48.8566,
            long=2.3522
        )
        self.consulte = ConsultePro.objects.create(
            idPro=self.pro,
            idPers=self.personne
        )
    
    def test_consulte_pro_creation(self):
        """Test de création d'une consultation de professionnel"""
        self.assertEqual(self.consulte.idPro, self.pro)
        self.assertEqual(self.consulte.idPers, self.personne)


# ============================================================================
# Tests des APIs (Views & Serializers)
# ============================================================================
