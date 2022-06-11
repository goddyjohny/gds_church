from django import forms
from .models import *

class ContributionForm(forms.ModelForm):
    
    class Meta:
        model = Contribution
        fields = '__all__'
        exclude = ['ref_no', 'balance']


class CashContributionForm(forms.ModelForm):
    
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
