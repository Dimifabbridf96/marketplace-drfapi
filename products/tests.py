from .models import Products
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class ProductListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='dimi', password='pass')

    def test_can_list_products(self):
        dimi = User.objects.get(username='dimi')
        response = self.client.get('/products/')
        Products.objects.create(owner=dimi, title='title')
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_logged_out_user_cant_create_product_posts(self):
        response = self.client.post('/products/', {'title': 'a title', 'description': 'a description'})
        count = Products.objects.count()
        self.assertEqual(count, 0)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProductDetailsViewTests(APITestCase):
    def setUp(self):
        dimi = User.objects.create_user(username='dimi', password='pass')
        alessia = User.objects.create_user(username='Alessia', password='word')

        Products.objects.create(owner=dimi, title='chair', description='ergonomic', category='Other')
        Products.objects.create(owner=alessia, title='makeup palette', description='bright and matty', category='Other')

    def test_can_show_detail_products_page(self):
        response = self.client.get('/products/1')
        self.assertEqual(response.data['title'], 'chair')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/products/999')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_user_cant_update_a_not_owned_product(self):
        self.client.login(username='dimi', password='pass')
        response = self.client.put('/products/2', {'title': 'amazing'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)




    
    

