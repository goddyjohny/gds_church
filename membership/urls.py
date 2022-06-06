from django.urls import path
from . import views

app_name = 'membership'


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

    path("list-member/", views.list_member, name="list-member"),
    path("add-member/", views.add_member, name="add-member"),
    path("update-member/<str:id>", views.update_member, name="update-member"),
    path("member-details/<str:id>", views.member_details, name="member-details"),
    
    path("list/dioceses", views.list_dioceses, name="list_dioceses"),
    path("add/diocese", views.add_diocese, name="add_diocese"),
    path("edit/diocese/<int:id>", views.edit_diocese, name="edit_diocese"),
    path("list/deacons", views.list_deacons, name="list_deacons"),
    path("add/deacon", views.add_deacon, name="add_deacon"),
    path("edit/deacon/<int:id>", views.edit_deacon, name="edit_deacon"),
    path("list/parishes", views.list_parishes, name="list_parishes"),
    path("add/parish", views.add_parish, name="add_parish"),
    path("edit/parish/<int:id>", views.edit_parish, name="edit_parish"),




]
