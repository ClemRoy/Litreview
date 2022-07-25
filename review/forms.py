from pyexpat import model
from django import forms
from review import models


class addFollowForm(forms.ModelForm):
    followed_user_name = forms.CharField(
        max_length=25, label="nom de l'utilisateur a suivre")

    class Meta:
        model = models.UserFollows
        fields = ["followed_user_name"]


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description","image"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ["headline","body","rating"]