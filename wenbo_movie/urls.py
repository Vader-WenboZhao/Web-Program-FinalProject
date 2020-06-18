from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("movies", views.all_movie, name="all_movie"),
    path("movies/<imdb_num>", views.movie, name="movie"),
    path("movies/<imdb_num>/review", views.review, name="review"),
    path("movies/<imdb_num>/like_m", views.like_m, name="like_m"),
    path("workers", views.all_worker, name="all_worker"),
    path("workers/<imdb_num>", views.worker, name="worker"),
    path("workers/<imdb_num>/like_w", views.like_w, name="like_w"),
]
