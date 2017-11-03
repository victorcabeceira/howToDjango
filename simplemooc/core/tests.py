from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class HomeViewTest(TestCase):

  def teste_home_status_code(self):
    client = Client()
    response = client.get(reverse('core:home'))
    self.assertEqual(response.status_code, 200)

  def test_home_template_user(self):
    client = Client()
    response = client.get(reverse('core:home'))
    self.assertTemplateUsed(response, 'base.html')
    self.assertTemplateUsed(response, 'home.html')
