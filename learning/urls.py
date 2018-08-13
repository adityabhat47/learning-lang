from django.urls import path
from .views import ListlanguagesView


urlpatterns = [
    path('languages/', ListlanguagesView.as_view(), name="languages-all")
]