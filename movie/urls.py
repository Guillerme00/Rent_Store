from django.urls import path
from .views import MovieView

urlpatterns = [
    path("movies/", MovieView.as_view(), name="movies"),
    path("movies/<int:pk>/", MovieView.as_view(), name="movies")
]