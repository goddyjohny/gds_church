from django.urls import path
from . import views 

app_name = 'finance'

urlpatterns = [
    path("list/cash/accounts", views.list_cash_accounts, name="list_cash_accounts"),
    path("list/contributions",
         views.list_contributions, name="list_contributions"),
    path("edit/<int:id>/contribution",
         views.edit_contribution, name="edit_contribution"),
    path("view/<int:id>/contribution",
         views.view_contribution, name="view_contribution"),
    path("add/<int:id>/cash/contribution",
         views.add_cash_contribution, name="add_cash_contribution"),
    path("add/<int:id>/pledge",
         views.add_pledge, name="add_pledge"),
    path("list/offering/divisions",
         views.list_offering_divisions, name="list_offering_divisions"),
    path("list/offerings",
         views.list_offerings, name="list_offerings"),
    path("activate/offering/divisions/<int:id>",
         views.activate_offering_divisions, name="activate_offering_divisions"),

    
]
