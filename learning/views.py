from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import languages
from .serializers import languagesSerializer


class ListlanguagesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = languages.objects.all()
    serializer_class = languagesSerializer