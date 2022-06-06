from django.db import models
from django.urls import reverse

# Create your models here.


class Diocese(models.Model):
    name = models.CharField(max_length=50,)
    address = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Diocese"
        verbose_name_plural = "Dioceses"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Diocese_detail", kwargs={"pk": self.pk})


class Deacon(models.Model):
    diocese = models.ForeignKey(
        Diocese, verbose_name="deacon", on_delete=models.CASCADE)
    name = models.CharField(max_length=50,)
    address = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Deacon"
        verbose_name_plural = "Deacons"

    def __str__(self):
        return self.name


class Parish(models.Model):
    deacon = models.ForeignKey(
        Deacon, verbose_name="parish", on_delete=models.CASCADE)
    name = models.CharField(max_length=50,)
    address = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Parish"
        verbose_name_plural = "Parishes"

    def __str__(self):
        return self.name

class Kigango(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Kanda(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    kigango = models.ForeignKey(Kigango, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Fellowship(models.Model):
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)
    kanda = models.ForeignKey(Kanda, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

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
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Member(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    birthdate = models.DateField()
    gender = models.CharField(max_length=8)
    phone = models.CharField(max_length=10, null=True)
    address = models.TextField()
    age_status = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=50, null=True)
    is_baptized = models.BooleanField('baptized', default=False)
    is_active = models.BooleanField('active', default=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.fullname









 
