from django.test import TestCase
from django.urls import reverse


class FrontPageTest(TestCase):
    def test_no_crash(self):
        url = reverse('frontpage')
        response = self.client.get(url)
        self.assertContains(response, 'template1')
