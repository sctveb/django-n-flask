from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from account.forms import ProfileForm
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('question:list')
    else:
        if request.method == "POST": # 사용자가 로그인을 요청했으면?
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                auth_login(request, form.get_user())
                return redirect('question:list')
        else: # 로그인을 위한 폼을 요청했으면?
            form = AuthenticationForm()
            
            return render(request,"account/login.html",{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('question:list')
    
def signup(request):
    if request.user.is_authenticated:
        return redirect('question:list')
    else:
        if request.method == "POST": # 사용자가 로그인을 요청했으면?
            form = UserCreationForm(request.POST)
            pro_form = ProfileForm(request.POST)
            if form.is_valid() and pro_form.is_valid():
                user = form.save()
                profile = pro_form.save(commit=False)
                profile.user = user
                profile.save()
                auth_login(request, user)
                return redirect('question:list')
        else: # 로그인을 위한 폼을 요청했으면?
            form = UserCreationForm()
            pro_form = ProfileForm()
        return render(request,"account/signup.html",{'form':form,"pro_form":pro_form})