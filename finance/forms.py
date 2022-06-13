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
        
        
        
        


class ContributionForm(forms.ModelForm):
    
    class Meta:
        model = Contribution
        fields = '__all__'
        exclude = ['ref_no', 'balance']


class CashContributionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.contribution = kwargs.pop("contribution")
        super(CashContributionForm, self).__init__(*args, **kwargs)
        self.fields['pledger'].queryset = Pledge.objects.filter(
            contribution=self.contribution)
        self.fields['pledger'].empty_label = "Select Pledger"
    
    class Meta:
        model = CashContribution
        fields = '__all__'
        exclude = ['ref_no', 'account', 'contribution', 'received_by']


class PledgeForm(forms.ModelForm):

    class Meta:
        model = Pledge
        fields = '__all__'
        exclude = ['completed' ,'contribution']


class OfferingDivisionForm(forms.ModelForm):
    
    class Meta:
        model = OfferingDivision
        fields = '__all__'
        exclude = ['active', ]


class OfferingForm(forms.ModelForm):

    class Meta:
        model = Offering
        fields = ['name', 'description', 'amount', ]

