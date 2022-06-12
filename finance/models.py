from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ExpenseName(models.Model):
    name = models.CharField(max_length=50,unique=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)     

    def __str__(self):
        return self.name  


class Expense(models.Model):
    name = models.ForeignKey(ExpenseName, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=10)  
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    is_debited = models.BooleanField('debit', default=False)

    def __str__(self):
        return self.name.name       



class Property(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Deposit(models.Model):
    prop =models.ForeignKey(Property,on_delete=models.CASCADE) 
    description = models.CharField(max_length=500)
    amount =  models.DecimalField(decimal_places=2, max_digits=10)  
    payment_method =models.CharField(max_length=50)
    account_no = models.CharField(max_length=50)
    bankname = models.CharField(max_length=50)
    depositor = models.ForeignKey(User,on_delete=models.CASCADE) 
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_credited = models.BooleanField('credit', default=False)
    

    def __str__(self):
        return self.prop.name


class CashAccount(models.Model):
    ref_no = models.CharField(max_length=100)
    description = models.TextField()
    debit = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    credit = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    # Below the mandatory fields for generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']
        verbose_name = "Cash Account"
        verbose_name_plural = "Cash Accounts"

    def __str__(self):
        return "{0}".format(self.ref_no,self.debit)

    def get_absolute_url(self):
        return reverse("CashAccount_detail", kwargs={"pk": self.pk}) 







