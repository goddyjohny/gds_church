from django.urls import path
from . import views

app_name = 'membership'

urlpatterns = [
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
