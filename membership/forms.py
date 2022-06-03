from django import forms


#forms start here

class KandaForm(forms.ModelForm):
    """Form definition for Kanda."""

    kanda =  block_no = forms.ModelChoiceField(label="Kanda", queryset=Kanda.objects.all())

    class Meta:
        """Meta definition for Kandaform."""

        model = Kanda
        fields = ('name','address','kigango')
