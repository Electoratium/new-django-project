from django import forms

class BaseForm(forms.Form):
    name  = forms.CharField(max_length=128)