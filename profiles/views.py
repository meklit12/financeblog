from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = RegisterForm()
    return render(request, "profiles/register.html", {"form": form})