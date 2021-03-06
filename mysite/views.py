from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tutorials
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
# Create your views here.
def homepage(request):
    form=Tutorials.objects.all()
    context={'form':form,'hello':_('Hello')}
    return render(request,'mysite/home.html',context=context)
def register(request):
    if request.method=='POST':

        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request,user)
            return redirect('mysite:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request,'mysite/signup.html',{'form':form})
    form = UserCreationForm()
    return render(request,'mysite/signup.html',{'form':form})

def logout_request(request):
    logout(request)
    messages.info(request," You have succesfully logged out")
    return redirect('mysite:homepage')

def login_request(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form=AuthenticationForm()
    return render(request,'mysite/login.html',{'form':form})

# from django.utils.translation import ugettext_lazy as _
# def localization(request):
#     context={'hello':_('Hello')}
#     return render(request,'mysite/home.html',context)
