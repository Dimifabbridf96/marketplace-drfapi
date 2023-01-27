from .models import Products
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class ProductListViewTests(APITestCase):
    def test_can_list_products(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_logged_user_can_create_product_posts(self):
        self.client.login(username='Dimi', password='pass')
        response = self.client.post('/products/', {'title': 'a title', 'description': 'a description'})
        count = Products.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_product_posts(self):
        response = self.client.post('/products/', {'title': 'a title', 'description': 'a description'})
        count = Products.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class ProductDetailsViewTests(APITestCase):
    def setUp(self):
         User.objects.create_user(username='Dimi', password='pass')

    
    

