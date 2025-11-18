
from django.urls import path
from . import views
from .views import list_books
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register


# URL configuration for relationship_app

urlpatterns = [
    path("books/", views.list_all_books, name="list_all_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]

# Additional URL patterns for user authentication


urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", register, name="register"),
]
