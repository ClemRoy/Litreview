from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import forms
from review.forms import addFollowForm
from django.contrib.auth.models import User
from authentication import models
# Create your views here.

@login_required
def home(request):
    return render(request, "review/home.html")

@login_required
def follows(request):
    form = forms.addFollowForm()
    message = ""
    if request.method == "POST":
        form = forms.addFollowForm(request.POST)
        if form.is_valid():
            user_to_add = form.cleaned_data["username"]
            if models.CustomUser.objects.filter(username=user_to_add).exists():
                message = "l'utilisateur existe"
            else:
                message = "L'utilisateur n'existe pas"

    return render(request, "review/follows.html", context={"form":form, "message":message})