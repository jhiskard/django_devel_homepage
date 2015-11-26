from django import forms
from app03.models import BoardModel

class BoardModelForm(forms.ModelForm):
    class Meta:
        model = BoardModel
        fields = '__all__'
