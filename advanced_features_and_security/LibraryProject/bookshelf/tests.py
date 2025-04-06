from django.test import TestCase, Client
from django.urls import reverse

class ExampleFormTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_example_form_renders(self):
        response = self.client.get(reverse('example_form'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_example_form_submission(self):
        response = self.client.post(reverse('example_form'), {
            'name': 'Rashad',
            'email': 'rashad@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Form submitted successfully!')
