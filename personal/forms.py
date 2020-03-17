from django import forms
from django.utils.translation import gettext_lazy as _
from django.core import validators
class Contact(forms.Form):
    name=forms.CharField(validators=[validators.MinLengthValidator(2,_("Please give a name with more than 2 characters"))])
    email=forms.EmailField(validators=[validators.EmailValidator(_("Please give a valid email"))])
    comment=forms.CharField(widget=forms.Textarea)