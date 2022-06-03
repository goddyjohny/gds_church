from django import forms
from .models import Kanda,Kigango, Parish


#forms start here




class KigangoForm(forms.ModelForm):
    """Form definition for Kanda."""

    parish = forms.ModelChoiceField(label="Parish", queryset=Parish.objects.all())

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
