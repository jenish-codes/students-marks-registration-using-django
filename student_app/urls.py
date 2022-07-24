from django.urls import path
from .views import AddDetails, Details


urlpatterns = [
    path('', AddDetails.as_view(), name="add"),
    path('details', Details.as_view(), name="details"),
]