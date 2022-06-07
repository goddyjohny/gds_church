from django import forms
from .models import *


#forms start here
class KigangoForm(forms.ModelForm):
    """Form definition for Kigango."""

    parish = forms.ModelChoiceField(label="Parokia", queryset=Parish.objects.all())

    class Meta:
        """Meta definition for Kigangoform."""

        model = Kigango
        fields = ('name','address','parish')

class KandaForm(forms.ModelForm):
    """Form definition for Kanda."""

    kigango = forms.ModelChoiceField(label="Kigango", queryset=Kigango.objects.all())

    class Meta:
        """Meta definition for Kandaform."""

        model = Kanda
        fields = ('name','address','kigango')


class FellowshipForm(forms.ModelForm):
    """Form definition for Fellowship."""

    kanda = forms.ModelChoiceField(label="Kanda", queryset=Kanda.objects.all())

    class Meta:
        """Meta definition for Fellowshipform."""

        model = Fellowship
        fields = ('name','address','kanda')       

        

class FamilyForm(forms.ModelForm):
    """Form definition for Family."""

    fellowship = forms.ModelChoiceField(label="Jumuiya", queryset=Fellowship.objects.all())
    ndoa = forms.BooleanField(label='Wanandoa (Weka Tiki Kama Wanandoa)',widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    class Meta:
        """Meta definition for Familyform."""

        model = Family
        fields = ('name','address','fellowship','phone','ndoa')     


class MemberForm(forms.ModelForm):
    """Form definition for Member."""
    gender_options = {
        ('Male', 'Male'),
        ('Female', 'Female'),
    } 

    agestatus_options = {
        ('Wawaka', 'Wawata'),
        ('Wawata', 'Wawata'),
        ('Walei', 'Walei'),
        ('Kiwawa', 'Kiwawa'),
        ('Utoto Mtakatifu', 'Utoto Mtakatifu'),
    }

    marital_options = {
        ('Mwanandoa', 'Mwanandoa'),
        ('Uchumba', 'Uchumba'),
        ('Single', 'Single'),
        ('Mtoto', 'Mtoto'),
    }


    family = forms.ModelChoiceField(label="Familia aliyopo", queryset=Family.objects.all())
    gender = forms.CharField(label='Jinsia', widget=forms.Select(choices=gender_options, attrs={'class': 'form-control'}))
    age_status = forms.CharField(label='Kikundi', widget=forms.Select(choices=agestatus_options, attrs={'class': 'form-control'}))
    marital_status = forms.CharField(label='Mahusiano', widget=forms.Select(choices=marital_options, attrs={'class': 'form-control'}))
    is_baptized = forms.BooleanField(label='Umebatizwa? (Weka Tiki Kama Umepata Ubatizo)',widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=False)
    phone = forms.CharField(required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))

    class Meta:
        """Meta definition for Memberform."""

        model = Member
        fields = ('fullname','birthdate','gender','phone','family','age_status','marital_status','address','is_baptized')

        widgets = {
        'birthdate': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }



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
