from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return redirect('dashboard')


def about(request):
    return render(request, 'about.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
