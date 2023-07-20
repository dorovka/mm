from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def test_33(request):
    return HttpResponse('ТЕСТ№33')

def top(request):
    return render(request, 'top-sellers.html')

def log(request):
    return render(request, 'login.html')

def reg(request):
    return render(request, 'register.html')

def prof(request):
    return render(request, 'profile.html')

def post(request):
    return render(request, 'advertisement-post.html')