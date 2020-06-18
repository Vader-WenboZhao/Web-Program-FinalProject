from django.urls import path

from . import views

urlpatterns = [
    path("user", views.user, name="user"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("register_jump", views.register_jump, name="register_jump"),
    path("search_view", views.search_view, name="search_view"),
    path("search", views.search, name="search"),
]
