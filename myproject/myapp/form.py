from .models import do
from django import forms


class myform(forms.ModelForm):
    class Meta:
        model = do()
        fields = ['name', 'priority', 'date']
