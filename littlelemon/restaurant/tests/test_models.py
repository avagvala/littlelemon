from django.test import TestCase
from ..models import Menu

class MenuTest(TestCase):
    def test_get_menu(self):
        menu = Menu.objects.create(Title="Ice Cream", Price=80, Inventory=100)
        self.assertEqual(str(menu), "Ice Cream : 80")