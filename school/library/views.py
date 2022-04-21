from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm
from .forms import bookregisteration
from .models import data, Record, hirebook
from . import models


# Create your views here.


def home(request):
    return render(request, 'first.html')


def view(request):
    books = data.objects.all()
    b = {"book": books}
    return render(request, 'view.html', b)


def books(request):
    books = data.objects.all()
    # return render(request,'books.html')
    return render(request, 'books.html', {'book': books})


# We add new items and show them
def add(request):
    if request.method == "POST":
        fm = bookregisteration(request.POST)
        if fm.is_valid():
            bn = fm.cleaned_data['book_name']
            an = fm.cleaned_data['author_name']
            pc = fm.cleaned_data['price']
            reg = data(book_name=bn, author_name=an, price=pc)
            reg.save()
            fm = bookregisteration()

    else:
        fm = bookregisteration()
    books = data.objects.all()
    return render(request, 'add.html', {'form': fm, 'book': books})


# This fun will delete data:
def delete_data(request, id):
    if request.method == "POST":
        pi = data.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/add.html')


# Updation and editing function:

def update_data(request, id):
    if request.method == "POST":
        pi = data.objects.get(pk=id)
        fm = bookregisteration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = data.objects.get(pk=id)
        fm = bookregisteration(instance=pi)

    return render(request, 'update.html', {'form': fm})


def signin(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f'WELCOME {username}')
            return redirect('signin')
        else:
            messages.info(request, f'Account does not exist please register yourself')
    form = AuthenticationForm()
    return render(request, 'signup.html')


def signup(request):
    try:
        if request.method == "POST":
            name = request.POST['ename']
            email = request.POST['email']
            mobile = request.POST['mobile']
            password = request.POST['pass']
            rpassword = request.POST['cpass']
            dob = request.POST['dob']
            Record(ename=name, email=email, mobile=mobile, password=password, dob=dob).save()
            d = Record.objects.all()
            return render(request, 'showdata.html', {'a': d})
        return render(request, 'signup.html')
    except:
        return render(request, 'error.html')


# ----------

def login1(request):
    if request.method == "POST":
        email = request.POST['email']
        passw = request.POST['password']
        try:
            e = Record.objects.get(email=email)
            p = Record.objects.get(password=passw)
            if e == p:
                return HttpResponseRedirect('add.html')
        except:
            return render(request, "login1.html", {'msg': 'invalid credential !!!'})
            # return HttpResponseRedirect('login1.html')
    else:
        return render(request, "login1.html")


# -------------------------

def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("signup")

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


# -----------------------------------------------------------------------------------------------------------------------------

def hire1(request):
    if request.method == "POST":
        sn = request.POST['student_name']
        bn = request.POST['book_name']
        bi = request.POST['book_id']
        hd = request.POST['hire_date']
        i_d = request.POST['issu_date']
        d = request.POST['due']
        hirebook(student_name=sn, book_name=bn, book_id=bi, hire_date=hd, issu_date=i_d, due=d).save()
        hbook = hirebook.objects.all()
        return render(request, "hirebook.html", {'hbook': hbook})
    # return render(request,"hirebook.html")
    hbook = hirebook.objects.all()
    return render(request, "hirebook.html", {'hbook': hbook})


def hdelete_data(request, id):
    if request.method == "POST":
        pi = hirebook.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/hirebook')


def hupdate_data(request, id):
    if request.method == "POST":
        pi = hirebook.objects.get(pk=id)
        fm = hirebook(request.POST, instance=pi)
        fm.save()
    else:
        pi = data.objects.get(pk=id)
        fm = hirebook(instance=pi)

    return render(request, '/add.html')
