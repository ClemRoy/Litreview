from django import forms
from review import models

class addFollowForm(forms.Form):
    username = forms.CharField(max_length=25)