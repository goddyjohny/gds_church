from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Document(models.Model):
    name = models.CharField(max_length=10, unique=True)
    files = models.FileField(upload_to='documents/%Y/%m/%d')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    shared_users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='shared_user')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
