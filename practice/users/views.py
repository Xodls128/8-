from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth 


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],)

            profile = Profile(
                user=user,
                nickname=request.POST['nickname'],
                image=request.FILES.get('profile_imange'),)

            profile.save() 
            auth.login(request,user)
            return redirect('home')  
        return render(request, template_name='signup.html') 
    return render(request, template_name='signup.html') 
    

def login(requst):
    if requst.method == 'POST':
        username = requst.POST['username']
        password = requst.POST['password']
        user =authenticate(requst, username=username, password=password)

        if user is not None:
            auth.login(requst, user)
            return redirect('home')
        return render(requst, template_name='login.html')
    return render(requst, template_name='login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
        