from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from main.forms import NewUserForm

def homepage(request):
    return render(request, "base.html", {})

def user_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="main/register.html", context={"register_form":form})