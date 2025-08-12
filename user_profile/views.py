from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def registers(request):
    if request.method == 'POST':
        form = forms.singUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'"User Created Successfully"')
            return redirect('home')
        
    else:
        form = forms.singUpForm()
    return render(request, 'register.html',{'form':form})

def profile(request):
    return render(request,'profile.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Login Successfully!!')
                login(request,user)
                return redirect("profile")
            else:
                messages.warning(request,"Login Innformation Incorect!!")
                return redirect('singup')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{"form":form})

def user_logout(request):
    logout(request)
    return redirect('home')


def profile_change(request):
    if request.method == 'POST':
        form = forms.ChangeProfile(request.POST, instance=request.user)   
        if form.is_valid():
            form.save()
            messages.success(request,'Your Profile Updated Successfully!!')
            return redirect('profile')
        
    else:
        form =forms.ChangeProfile(instance=request.user)
        
    return render(request,'changesPass.html',{'form':form})
                
