from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth #auth들어간 것은 인증에 관련된 것

#회원가입
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )

            profile = Profile(
                user=user,
                nickname=request.POST['nickname'],
                image=request.FILES.get('profile_imange'),
            )

            profile.save() #user은 장고에서 기본으로 제공하는 객체라 save필요 없음  #근데 profile은 우리가 만든 객체라 save필요
            auth.login(request,user)
            return redirect('home') #로그인하면 home으로 
        return render(request, template_name='signup.html') # 비밀번호1,2가 일치하지 않을 때 다시 회원가입화면 렌더링
    return render(request, template_name='signup.html') # POST요청으로 오지 않았을 때도 회원가입화면 렌더링
    
#로그인
def login(requst):
    if requst.method == 'POST' :
        username = requst.POST['username']
        password = requst.POST['password']
        user = authenticate(requst, username=username, password=password) #장고한테 일치하는지 확인해주라고 요청

        if user is not None:
            auth.login(requst, user)
            return redirect('home') # user가 None이 아니면(=정상적인 로그인) home으로 리다이렉트
        return render(requst, template_name='login.html') #user가 None이면 회원정보 없거나 오류라서 다시 로그인화면 뿌려줌
    return render(requst, template_name='login.html')# POST요청이 아니어도 로그인화면 보여줌

#로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')
        