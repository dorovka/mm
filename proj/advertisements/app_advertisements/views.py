from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('УСПЕХ')

def test_33(request):
    return HttpResponse('ТЕСТ№33')