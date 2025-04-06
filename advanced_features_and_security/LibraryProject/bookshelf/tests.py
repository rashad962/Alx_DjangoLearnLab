from django.test import TestCase, Client
from django.urls import reverse

class SecurityTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_csrf_token_present(self):
        response = self.client.get(reverse('book_list'))
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_xss_protection_header(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response['X-Frame-Options'], 'DENY')

    def test_csp_header(self):
        response = self.client.get(reverse('book_list'))
        self.assertIn('Content-Security-Policy', response)
