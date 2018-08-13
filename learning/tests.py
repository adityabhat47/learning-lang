from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import languages
from .serializers import languagesSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_language(title="", complexity=""):
        if title != "" and complexity != "":
            languages.objects.create(title=title, complexity=complexity)

    def setUp(self):
        # add test data
        self.create_language("Hindi", "Hard")
        self.create_language("Marathi", "medium")
        self.create_language("English", "Easy")
        self.create_language("Telugu", "Hard")


class GetAlllanguagesTest(BaseViewTest):

    def test_get_all_languages(self):
        """
        This test ensures that all languages added in the setUp method
        exist when we make a GET request to the languages/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("languages-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = languages.objects.all()
        serialized = languagesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)