from django.test import TestCase
from django.urls import reverse
from ..models import Menu
from ..serializers import MenuSerializer
from rest_framework import status
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of Menu model
        Menu.objects.create(Title='Item 1', Price=10.50, Inventory=20)
        Menu.objects.create(Title='Item 2', Price=15.75, Inventory=15)
        Menu.objects.create(Title='Item 3', Price=8.99, Inventory=30)

    def test_getall(self):
        # Initialize API client
        client = APIClient()
        
        # Make GET request to retrieve all Menu objects
        response = client.get('http://127.0.0.1:8000/restaurant/menu/')

        # Retrieve all Menu objects from the database
        menus = Menu.objects.all()
        
        # Serialize the Menu objects
        serializer = MenuSerializer(menus, many=True)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized data in the response matches the expected serialized data
        self.assertEqual(response.data, serializer.data)
