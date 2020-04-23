from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from ToDoApp.forms import *
from django.http import HttpResponse , HttpResponseRedirect
from ToDoApp.models import main as m
# Create your views here.

def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")


def registrationPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        

    context = {'form':form}
    return render(request, 'registration.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return redirect('login')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def main(request):
    tasks = m.objects.all()
    form = mainform()

    if request.method == "POST":
        form = mainform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')   

    return render(request,'main.html',{'tasks':tasks,'form':form})

def updateTask(request, pk):
	task = m.objects.get(id=pk)

	form = mainform(instance=task)

	if request.method == 'POST':
		form = mainform(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('main')

	return render(request, 'update.html', context={'form':form})

def deleteTask(request, pk):
	item = m.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('main')

	return render(request, 'delete.html', context = {'item':item})