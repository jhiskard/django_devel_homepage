from django import forms
from app02.models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'
