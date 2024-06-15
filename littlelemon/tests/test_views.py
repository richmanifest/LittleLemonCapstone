from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from django.contrib.auth.models import User





class MenuViewTest(TestCase):
    def setup(self):
        self.burger = Menu.objects.create(title='Burger', price=9.00, inventory=5)
        self.pasta = Menu.objects.create(title='Pasta', price=14.00, inventory=5)
        self.lemonade = Menu.objects.create(title='Lemonade', price=2.50, inventory=5)


    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()

    def test_getall(self):
        url = reverse('menu-list')
        # Authenticate the client with the created user
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Ensure the request was successful
        response_data = response.data
        menu_items = Menu.objects.all()
        serialized_data = MenuSerializer(menu_items, many=True).data
        self.assertEqual(response_data, serialized_data)


