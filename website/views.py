from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm, AddRecordForm
from django.http import HttpResponse
from .models import Rocord



# Create your views here.
def home(request):
    # bring the record to the web page
    records = Rocord.objects.all()
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
        return  render(request, 'home.html',{'records':records})
# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"you have been logged out ...")
    return redirect('home')


def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            #authenticate and login 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, 'you are saved in our application welcom!!!')
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    
    return render(request, 'register.html', {'form':form})

def customer_record(request,pk):

    if request.user.is_authenticated:

        customer_record = Rocord.objects.get(id = pk)
        return render(request,'record.html',{'customer_record': customer_record})
    
    else:
        messages.success(request, 'you must be loggin to see this page....')
        return redirect('home')
    

def delete_customer(request, pk):

    if request.user.is_authenticated:
        delete_it = Rocord.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record Deleted Successfuly !!")
        return redirect('home')
    else:
        messages.success(request,"You must Be Logged In to delete that person....")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added ....")
                return redirect('home')
        return render(request, 'add_record.html',{'form' : form})
    
    else:
        messages.success(request, "you must be loggin to be able to add record")
        return redirect('home')


def update_customer(request, pk):

    if request.user.is_authenticated:
        curent_record = Rocord.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance = curent_record)
        if form.is_valid():
            form.save()
            messages.success(request, "record has been updated!")
            return redirect('home')
        return render(request, 'update_record.html',{'form':form})
    else:
        messages.success(request, "you must be loggin to be able to add record")
        return redirect('home')