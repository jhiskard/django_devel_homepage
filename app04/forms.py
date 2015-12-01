from django import forms
from app04.models import StructureModel

class StructureForm(forms.ModelForm):
    class Meta:
        model = StructureModel
        fields = ('structure', 'description', 'commands', 'created')
