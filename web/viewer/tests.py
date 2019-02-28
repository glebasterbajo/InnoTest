# Django Modules
from django.test import TestCase


class ViewerIndexViewTests(TestCase):
    def test_status_code_and_images(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context["images"], [])
