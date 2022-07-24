from django.urls import path
from .views import AddDetails, Details, delete, Update


urlpatterns = [
    path('', AddDetails.as_view(), name="add"),
    path('details/', Details.as_view(), name="details"),
    path('update/<int:id>/', Update.as_view(), name="update"),
    path('delete/<int:id>/', delete, name="delete"),
]