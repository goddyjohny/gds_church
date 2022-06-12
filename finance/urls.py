from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path("category/", views.expense_category, name="category"),
    path("update-category/<str:id>", views.expense_category_updates, name="update-category"),

    path("expense-name/", views.expense_categoryname, name="expense-name"),
    path("update-expense-name/<str:id>/", views.update_expense_categoryname, name="update-expensename"),

    path("expense/", views.expense, name="expense"),
    path("update-expense/<str:id>/", views.update_expense, name="update-expense"),
    path("debit-account/<str:id>/", views.expense_debit, name="debit-account"),

    path("property/", views.property, name="property"),
    path("update-property/<str:id>/", views.update_property, name="update-property"),


    path("deposit/", views.deposit, name="deposit"),
    path("update-deposit/<str:id>/", views.update_deposit, name="update-deposit"),
    path("credit-account/<str:id>/", views.deposit_credit, name="credit-account"),

    path("list/cash/accounts", views.list_cash_accounts, name="list_cash_accounts"),






]
