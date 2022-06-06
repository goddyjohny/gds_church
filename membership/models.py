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

 
