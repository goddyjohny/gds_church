from django.db import models

# Create your models here.

class Parish(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name



class Kigango(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField()

    def __str__(self) -> str:
        return self.name


class Kanda(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    kigango = models.ForeignKey(Kigango, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField()

    def __str__(self) -> str:
        return self.name


class Fellowship(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    kigango = models.ForeignKey(Kigango, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField()

    def __str__(self) -> str:
        return self.name


class Family(models.Model):
    fellowship = models.ForeignKey(Fellowship, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    ndoa = models.BooleanField('ndoa',default=False)
    is_active = models.BooleanField('active',default=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField()

    def __str__(self) -> str:
        return self.name


class Member(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    birthdate = models.DateField()
    phone = models.CharField(max_length=10, null=True)
    address = models.TextField()
    age_status = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=50, null=True)
    is_baptized = models.BooleanField('baptized', default=False)
    is_active = models.BooleanField('active', default=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField()

    def __str__(self) -> str:
        return self.fullname







