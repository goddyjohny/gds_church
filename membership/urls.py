from django.urls import path
from . import views


urlpatterns = [
    path("add-kanda/", views.add_kanda, name="add-kanda"),
    path("update-kanda/<str:id>", views.update_kanda, name="update-kanda"),


    path("add-kigango/", views.add_kigango, name="add-kigango"),
    path("update-kigango/<str:id>", views.update_kigango, name="update-kigango"),


    path("add-fellowship/", views.add_fellowship, name="add-fellowship"),
    path("update-fellowship/<str:id>", views.update_fellowship, name="update-fellowship"),

    path("list-family/", views.list_family, name="list-family"),
    path("add-family/", views.add_family, name="add-family"),
    path("update-family/<str:id>", views.update_family, name="update-family"),
    
]
