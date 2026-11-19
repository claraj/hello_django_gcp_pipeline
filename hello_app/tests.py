from django.test import SimpleTestCase  # Does not attempt to set up a test database
from django.urls import reverse

class TestHomePage(SimpleTestCase):

    def test_hello_page_message(self):
        response = self.client.get(reverse('hello'))
        self.assertContains(response, 'HELLO')  # Or the message your app displays 




