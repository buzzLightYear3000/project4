from django.urls import path
from .views import CuisineListView

# /genres/
urlpatterns = [
    path('', CuisineListView.as_view())
]