from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PLACE, TEAM
from django.contrib import messages

# Create your views here.
# def place(request):
#    return render(request,"index.html")
def demo(request):
    obj = PLACE.objects.all()
    obj1 = TEAM.objects.all()
    return render(request,"index.html",{'result': obj, 'result1' : obj1})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

            user.save();

        else:
            messages.info(request, 'password not match')
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")









