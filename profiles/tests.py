from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase

class ProfileListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='Dimi', password='pass')

    def test_can_list_profiles(self):
        dimi = User.objects.get(username='Dimi')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_get_profile_details(self):
        dimi = User.objects.get(username='Dimi')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
