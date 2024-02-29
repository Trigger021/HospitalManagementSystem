from django.shortcuts import render, redirect
from hospitalapp.models import Member, Contact


# Create your views here.


def index(request):
    if request.method == 'POST':
        messages = Contact(name=request.POST['name'],
                           email=request.POST['email'],
                           subject=request.POST['subject'],
                           message=request.POST['message'], )

        messages.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


def inner(request):
    return render(request, 'inner-page.html')


def register(request):
    if request.method == 'POST':
        members = Member(Username=request.POST['username'],
                         Email=request.POST['email'],
                         password=request.POST['password'])

        members.save()
        return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def upload(request):
    return render(request, 'upload.html')


def details(request):
    messages = Contact.objects.all()
    return render(request, 'details.html', {'messages': messages})