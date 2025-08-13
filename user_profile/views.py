from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from cars.models import Cars
from .models import Purchase
from django.contrib.auth.decorators import login_required
from django.db.models import F

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
@login_required
def profile(request):
    user = request.user 
    purchases = Purchase.objects.filter(user=user).select_related('product')
    
    return render(request,'profile.html',{'purchases':purchases})

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
@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
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
@login_required                
def buy_now(request,id):
    product = get_object_or_404(Cars,id=id)
    
    if product.quantity<=0:
        messages(request,"Out of stock")
        return redirect("home")
    updated = Cars.objects.filter(id=id,quantity__gte=1).update(quantity=F('quantity')-1)
    if updated:
        Purchase.objects.create(user=request.user, product=product, quantity=1)
        return redirect('profile')
    else:
        messages(request,"Out of stock")
        return redirect("home")
        