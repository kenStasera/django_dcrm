from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def home(request):
    #check to see if logging in 
    if request.method == 'POST':
        username = request.POST['first_name']
        password = request.POST['password']

        #AUTHENTICATE
        user = authenticate(request, username = username,password =password)
        if user is not None:
            login(request,user)
            messages.success(request, "you have been Logged In ")
            return redirect ('home')
        else:
            messages.success(request, 'There was an error in loggin process, please try again')
            return redirect ('home')
    else :
        return  render(request, 'home.html',{})
# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out ...")
    return redirect('home')


def register_user(request):

    return render(request, 'register.html',{})