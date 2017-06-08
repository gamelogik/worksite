from django import forms

from django.forms import ModelForm
from django.core import validators
from .models import Cvs


def must_be_empty(value):
    if value:
        raise forms.ValidationError('is not empty')

class ApplyForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    verify_email = forms.EmailField(label="Please verify your email address", widget=forms.TextInput(attrs={'class':'form-control'}))
    motivation = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    honeypot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               label="Leave empty",
                               validators=[must_be_empty])
    class Meta:
        model = Cvs
        fields = ['name', 'email', 'motivation']

    def clean(self):
        cleaned_data = super(ApplyForm, self).clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('verify_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields"
            )

