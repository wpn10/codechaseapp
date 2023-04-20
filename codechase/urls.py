from django.urls import path

from . import views

urlpatterns = [
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("questions", views.questions, name="questions"),
    path("submissions", views.submissioins, name="submissions"),
]
