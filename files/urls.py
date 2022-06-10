from django.urls import path
from . import views

app_name = 'files'


urlpatterns = [
    path("upload-files/", views.upload_file, name="files-upload"),
    # path("update-file/<str:id>", views.update_file, name="files-update"),


]
