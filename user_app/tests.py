from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class RegisterTestCase(APITestCase):
  """Ensure that new user can successfully register"""
  def test_register(self):
    data = {
      "username": "testcase",
      "email": "testcase@gmail.com",
      "password": "test123",
      "password2": "test123"
    }
    response = self.client.post(reverse('register'),data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


class LoginLogoutTestCase(APITestCase):

  def setUp(self):
    self.user = User.objects.create_user(username="test_user", password="test123")

  def test_login(self):
    data = {
      "username": "test_user",
      "password": "test123"
    }
    response = self.client.post(reverse('login'), data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
