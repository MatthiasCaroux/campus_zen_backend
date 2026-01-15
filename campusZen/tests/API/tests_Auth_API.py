from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from campusZen.models import Personne


class AuthTests(APITestCase):
    """Tests d'authentification"""

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("token_obtain_pair")

    def test_register_user(self):
        """Test d'inscription d'un utilisateur"""
        data = {
            "emailPers": "test@example.com",
            "passwordPers": "securepassword123",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Personne.objects.filter(emailPers="test@example.com").exists())

    def test_register_user_with_role(self):
        """Test d'inscription avec un rôle spécifique"""
        data = {
            "emailPers": "admin@example.com",
            "passwordPers": "adminpass123",
            "role": "admin"
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = Personne.objects.get(emailPers="admin@example.com")
        self.assertEqual(user.role, "admin")

    def test_register_get_method(self):
        """Test de la méthode GET sur l'endpoint register"""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("message", response.data)

    def test_login_user(self):
        """Test de connexion d'un utilisateur"""
        user = Personne.objects.create(emailPers="login@example.com")
        user.set_password("mypassword")
        user.save()

        data = {
            "emailPers": "login@example.com",
            "password": "mypassword",
        }
        response = self.client.post(self.login_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["idPers"], user.idPers)
        self.assertIn("endAccess", response.data)
        self.assertIn("endRefresh", response.data)

    def test_login_wrong_password(self):
        """Test de connexion avec un mauvais mot de passe"""
        user = Personne.objects.create(emailPers="wrong@example.com")
        user.set_password("correctpassword")
        user.save()

        data = {
            "emailPers": "wrong@example.com",
            "password": "wrongpassword",
        }
        response = self.client.post(self.login_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("detail", response.data)

    def test_login_missing_password(self):
        """Test de connexion sans mot de passe"""
        user = Personne.objects.create(emailPers="missing@example.com")
        user.set_password("somepassword")
        user.save()

        data = {
            "emailPers": "missing@example.com",
        }
        response = self.client.post(self.login_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)

    def test_login_missing_email(self):
        """Test de connexion sans email"""
        data = {
            "password": "somepassword",
        }
        response = self.client.post(self.login_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_nonexistent_user(self):
        """Test de connexion avec un utilisateur inexistant"""
        data = {
            "emailPers": "nonexistent@example.com",
            "password": "password123",
        }
        response = self.client.post(self.login_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
