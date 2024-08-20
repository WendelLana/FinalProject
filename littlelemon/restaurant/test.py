from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Menu
from .serializers import MenuSerializer

class MenuTest(TestCase):
  def test_get_item(self):
    item = Menu.objects.create(title="IceCream", price=80, inventory=100, description='Cold dessert')
    self.assertEqual(str(item), "IceCream : 80")
  
  def setUp(self):
    # Set up test data for Menu model
    self.client = APIClient()
    self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
    self.item2 = Menu.objects.create(title="Burger", price=150, inventory=50)
    self.item3 = Menu.objects.create(title="Pizza", price=200, inventory=75)

  def test_getall(self):
    # Make a GET request to retrieve all Menu objects
    response = self.client.get(reverse('menu'))  # Assume 'menu' is the name of the URL pattern

    # Serialize the data manually
    items = Menu.objects.all()
    serializer = MenuSerializer(items, many=True)

    # Assert that the response status is 200 OK
    self.assertEqual(response.status_code, status.HTTP_200_OK)