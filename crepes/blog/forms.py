from django import forms
from .models import MiniURL,Personne

class MiniURLForm(forms.ModelForm):
    class Meta:
        model = MiniURL
        fields = ('url', 'pseudo')

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ('nom', 'prenom')
