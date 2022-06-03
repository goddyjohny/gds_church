from django.urls import path
from . import views


urlpatterns = [
    path("add-kanda/", views.add_kanda, name="add-kanda"),
    path("update-kanda/<str:id>", views.update_kanda, name="update-kanda"),


    path("add-kigango/", views.add_kigango, name="add-kigango"),
    path("update-kigango/<str:id>", views.update_kigango, name="update-kigango"),
    
]
