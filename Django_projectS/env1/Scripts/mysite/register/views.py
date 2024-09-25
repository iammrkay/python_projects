from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.
def register(respoonse):
    if respoonse.method == "POST":
        form = RegisterForm(respoonse.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(respoonse, "register/register.html", {"form":form})
