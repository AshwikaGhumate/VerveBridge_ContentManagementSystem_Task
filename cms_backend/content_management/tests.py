from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from content_management.models import Page

User = get_user_model()

class PageAPITestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        # Creating a client and authenticating
        self.client = APIClient()
        self.token = self.get_jwt_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Creating test data
        self.page = Page.objects.create(
            title='Test Page',
            slug='test-page',
            page_type='index',
            content='This is a test page content.'
        )

    def get_jwt_token(self):
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpassword'
        }, format='json')
        return response.data['access']

    def test_get_pages(self):
        response = self.client.get('/api/pages/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Page')

    def test_create_page(self):
        response = self.client.post('/api/pages/', {
            'title': 'New Page',
            'slug': 'new-page',
            'page_type': 'contact',
            'content': 'This is a new page content.'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Page')

    def test_update_page(self):
        response = self.client.put(f'/api/pages/{self.page.id}/', {
            'title': 'Updated Page',
            'slug': 'updated-page',
            'page_type': 'about',
            'content': 'This is updated page content.'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Page')

    def test_delete_page(self):
        response = self.client.delete(f'/api/pages/{self.page.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/api/pages/')
        self.assertEqual(len(response.data), 0)

    def test_authentication_required(self):
        self.client.credentials()  # Clear authentication
        response = self.client.get('/api/pages/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
