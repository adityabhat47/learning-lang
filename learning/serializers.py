from rest_framework import serializers
from .models import languages


class languagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = languages
        fields = ("title", "complexity")