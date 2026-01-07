from django.test import TestCase
from campusZen.models import Ressource


class RessourceModelTest(TestCase):
    """Tests pour le modèle Ressource"""
    
    def setUp(self):
        self.ressource = Ressource.objects.create(
            typeR="article",
            titreR="Gestion du stress",
            descriptionR="Un article sur la gestion du stress",
            lienR="https://example.com/stress"
        )
    
    def test_ressource_creation(self):
        """Test de création d'une ressource"""
        self.assertEqual(self.ressource.typeR, "article")
        self.assertEqual(self.ressource.titreR, "Gestion du stress")
        self.assertEqual(self.ressource.descriptionR, "Un article sur la gestion du stress")
        self.assertEqual(self.ressource.lienR, "https://example.com/stress")
    
    def test_ressource_str(self):
        """Test de la méthode __str__ de Ressource"""
        expected = f"{self.ressource.titreR} - {self.ressource.typeR}"
        self.assertEqual(str(self.ressource), expected)
    
    def test_ressource_type_choices(self):
        """Test des choix de type de ressource"""
        valid_types = ['article', 'video', 'podcast', 'livre', 'site_web', 
                       'documentaire', 'film', 'formation', 'autre']
        for type_r in valid_types:
            ressource = Ressource.objects.create(
                typeR=type_r,
                titreR=f"Test {type_r}",
                descriptionR="Description test",
                lienR="https://example.com"
            )
            self.assertEqual(ressource.typeR, type_r)
