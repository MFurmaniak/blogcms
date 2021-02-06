from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

@login_required
def index(request):
    if request.user.is_superuser:
        return redirect("/edit")
    else:
            return redirect("/")
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            if request.user.is_superuser:
                return redirect("/edit")
            else:
                return redirect("/")
    context['form']=form
    return render(request,'registration/sign_up.html',context)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form":form})