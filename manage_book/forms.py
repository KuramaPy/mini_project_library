from django import forms
from .models import book

class TaskForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['name', 'author', 'year_publication','category','pages','price',]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'author': forms.TextInput(attrs={'class': 'form-control',}),
            'year_publication': forms.DateInput(attrs={'class': 'form-control',}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control',}),
            'price': forms.NumberInput(attrs={'class': 'form-control',}),
        }