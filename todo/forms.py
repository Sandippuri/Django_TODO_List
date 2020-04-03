from django import forms 

class todoform(forms.Form):
    text = forms.CharField(max_length=40,
    widget=forms.TextInput(attrs={'placeholder': 'Enter todo e.g Building a webiste'}))