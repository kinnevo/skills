from django import forms
from .models import Genre


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ['name', 'skill_type', 'description', 'context']
