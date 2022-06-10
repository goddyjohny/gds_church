from django.urls import path, include
from . import views
app_name = 'accounts'

urlpatterns = [
    path("", views.userlogin, name="login"),
    path('logout/', views.userlogout, name='logout'),
    
]
