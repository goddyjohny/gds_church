from django import forms
from .models import *


#forms start here

class ExpenseCategoryForm(forms.ModelForm):
    """Form definition for ExpanseCategory."""

    class Meta:
        """Meta definition for ExpanseCategoryform."""

        model = ExpenseCategory
        fields = ('name','description')


class ExpenseNameForm(forms.ModelForm):
    """Form definition for ExpenseName."""

    category = forms.ModelChoiceField(label="Category", queryset=ExpenseCategory.objects.all())

    class Meta:
        """Meta definition for ExpenseNameform."""

        model = ExpenseName
        fields = ('name','category')


class ExpenseForm(forms.ModelForm):
    """Form definition for Expense."""

    name = forms.ModelChoiceField(label="Name", queryset=ExpenseName.objects.all())

    class Meta:
        """Meta definition for Expenseform."""

        model = Expense
        fields = ('name','description','amount')



class PropertyForm(forms.ModelForm):
    """Form definition for Property."""

    class Meta:
        """Meta definition for Propertyform."""

        model = Property
        fields = ('name','description',)


class DepositForm(forms.ModelForm):
    """Form definition for Deposit."""
    prop = forms.ModelChoiceField(label="Huduma", queryset=Property.objects.all())

    class Meta:
        """Meta definition for Depositform."""

        model = Deposit
        fields = ('prop','description','amount','payment_method','account_no','bankname',)
        
        
        
        

