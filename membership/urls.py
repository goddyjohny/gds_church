from django.urls import path, include
from . import views


urlpatterns = [
    path("add-kanda/", views.add_kanda, name="add-kanda"),
    
]
