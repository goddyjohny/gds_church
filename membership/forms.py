from django import forms
from .models import Kanda,Kigango, Parish,Fellowship, Family


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

    class Meta:
        """Meta definition for Familyform."""

        model = Family
        fields = ('name','address','fellowship','phone','ndoa')             
