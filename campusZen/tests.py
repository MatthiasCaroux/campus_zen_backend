from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Personne

# Create your tests here.


class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")

    def test_register_user(self):
        data = {
            "emailPers": "test@example.com",
            "passwordPers": "securepassword123",
        }
        response = self.client.post(self.register_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Personne.objects.filter(emailPers="test@example.com").exists())

    def test_login_user(self):
        user = Personne.objects.create(emailPers="login@example.com")
        user.set_password("mypassword")
        user.save()

        data = {
            "emailPers": "login@example.com",
            "passwordPers": "mypassword",
        }
        response = self.client.post(self.login_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["idPers"], user.idPers)
