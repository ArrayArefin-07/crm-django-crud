from django.shortcuts import render, redirect

from . forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages

# Create your views here.

#Homepge..
def home(request):
    return render(request,'webapp/index.html')


#Registern user here..

def register(request):
    frm = CreateUserForm()
    if request.method =="POST":
        frm = CreateUserForm(request.POST)

        if frm.is_valid():
            frm.save()
            messages.success(request,"Your Account created successfully.!")
            return redirect('my-login')
    
    context ={'frm':frm}
    return render (request, 'webapp/register.html', context=context)

#Login User...

def my_login(request):
    frm = LoginForm()
    if request.method == "POST":
        frm = LoginForm(request, data=request.POST)

        if frm.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request,user)

                messages.success(request,"You are now logged in.")
                return redirect('dashboard')

    context = {'frm':frm}
    return render(request,"webapp/my-login.html", context)

# Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()
    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)


# Create a record

@login_required(login_url='my-login')
def create_record(request):
    frm = CreateRecordForm()
    if request.method == "POST":
        frm = CreateRecordForm(request.POST)
        if frm.is_valid():
            frm.save()

            messages.success(request,'Your record has been created!')

            return redirect("dashboard")
        
    context = {'frm': frm}
    return render(request, 'webapp/create-record.html', context=context)
 

# Edit/UPDATE a record
@login_required(login_url="my-login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    frm = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        frm =UpdateRecordForm(request.POST, instance=record)
        if frm.is_valid():
            frm.save()

            messages.success(request,"The record was successfully updated.")

            return redirect('dashboard')
    context = {'frm':frm}
    return render (request,'webapp/update-record.html', context=context)

#READ/View a singular record
@login_required(login_url='my-login')
def singular_record(request,pk):
    all_records = Record.objects.get(id=pk)
    context = {'record':all_records}
    return render (request,"webapp/view-record.html", context=context)


# Delete record

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Successfully deleted the record")
    return redirect("dashboard")








#LogoutUser

def user_logout(request):
    auth.logout(request)
    messages.info(request, "You have been logged out!") #.success
    return redirect("my-login")

