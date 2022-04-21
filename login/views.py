from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth
from django.contrib import messages


# Create your views here.
def login1(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials try again')
            return redirect('login')
    else:
        return render(request,'login/login.html')