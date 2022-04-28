from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from core.api import serializers
from core import models

class EquipementsTestCase(APITestCase):
  
  def setUp(self):
    self.user = User.objects.create_user(username="example",password = "password123")
    self.token = Token.objects.get(user__username="example")
    self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
    self.categories = models.Categories.objects.create(name="electronics", slug="electronics", description="electric device")


  def test_equipements_list(self):
    response = self.client.get(reverse('EquipementsList'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)