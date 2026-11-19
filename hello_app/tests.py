from django.test import SimpleTestCase  # Does not attempt to set up a test database
from django.urls import reverse

# Create your tests here.
class TestHomePage(SimpleTestCase):

    def test_hello_page_message(self):
        response = self.client.get(reverse('hello'))
        self.assertContains(response, 'HELLO')