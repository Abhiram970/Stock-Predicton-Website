from django.shortcuts import redirect, render
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name  = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email1']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if (User.objects.filter(username = username).exists()):
                messages.info(request,'Username taken try again')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken try again')
                return redirect('register')
            else:    
                user = User.objects.create_user(username = username , password = password1 , email = email , first_name = first_name, last_name = last_name)
                user.save()
                print("User is created")
                return redirect('login')
        
        else:
            messages.info(request,'Password not matching try again')
            return redirect('register')
    
    else:
        return render(request,'register/register.html')