from django import forms
from .models import Kanda,Kigango


#forms start here

class KandaForm(forms.ModelForm):
    """Form definition for Kanda."""

    kigango = forms.ModelChoiceField(label="Kigango", queryset=Kigango.objects.all())

    class Meta:
        """Meta definition for Kandaform."""

        model = Kanda
        fields = ('name','address','kigango')
