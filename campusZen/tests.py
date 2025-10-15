from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Personne


class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("token_obtain_pair")

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
            "password": "mypassword",
        }
        response = self.client.post(self.login_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
        self.assertEqual(response.data["idPers"], user.idPers)

    def test_login_wrong_password(self):
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

    def test_login_missing_passwordPers(self):
        user = Personne.objects.create(emailPers="missing@example.com")
        user.set_password("somepassword")
        user.save()

        data = {
            "emailPers": "missing@example.com",
            # "passwordPers" absent pour tester la validation
        }
        response = self.client.post(self.login_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("password", response.data)
