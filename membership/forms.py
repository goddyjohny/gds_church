from django import forms
from .models import Kanda,Kigango, Parish,Fellowship


#forms start here




class KigangoForm(forms.ModelForm):
    """Form definition for Kanda."""

    parish = forms.ModelChoiceField(label="Parokia", queryset=Parish.objects.all())

    class Meta:
        """Meta definition for Kandaform."""

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
    """Form definition for Kanda."""

    kanda = forms.ModelChoiceField(label="Kanda", queryset=Kanda.objects.all())

    class Meta:
        """Meta definition for Kandaform."""

        model = Fellowship
        fields = ('name','address','kanda')        
