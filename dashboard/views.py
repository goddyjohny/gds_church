from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='accounts:login')
def index(request):
    context ={}
    return render(request, 'index.html', context)
    
