from django import forms
from .models import *


class DioceseForm(forms.ModelForm):

    class Meta:
        model = Diocese
        fields = '__all__'


class DeaconForm(forms.ModelForm):
    
    class Meta:
        model = Deacon
        fields = '__all__'


class ParishForm(forms.ModelForm):

    class Meta:
        model = Parish
        fields = '__all__'
