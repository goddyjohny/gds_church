from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
    """Form definition for Files."""
    files = forms.FileField(widget=forms.FileInput())
    shared_users = forms.ModelChoiceField(label="Share To (Dont Select if you dont Share)", queryset=User.objects.all(),required=False)


    class Meta:
        """Meta definition for Filesform."""

        model = Document
        fields = ('name','files','shared_users')








