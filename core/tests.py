"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse
import photos

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


# a kind of TestCase        
class AppIndexViewTest(TestCase):
    def test(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class GetLocationNameTest(TestCase):
    def test_valid_location_id(self):
        name = photos.get_location_name(1508229)
        self.assertEqual(name, u'Juan Valdez Caf\xe9')

    def test_invalid_location_id(self):
        name = photos.get_location_name("butthole")
        self.assertEqual(name, None)
