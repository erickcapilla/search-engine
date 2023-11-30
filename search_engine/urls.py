from django.urls import path
from search_engine import views

urlpatterns = [
    path("", views.home, name="home"),
]