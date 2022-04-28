import imp
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import auth
# Create your views here.
from django.http import HttpResponseRedirect
import time

def home(request):
    return render(request, 'home/index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')