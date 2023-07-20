from django.urls import path
from .views import index, test_33, top, prof, reg, log, post

urlpatterns = [
    path('', index, name = '/'),
    path('test33/', test_33),
    path('top-sell', top, name = 'top'),
    path('profile', prof, name = 'prof'),
    path('register', reg, name = 'reg'),
    path('login', log, name = 'log'),
    path('post', post, name = 'post'),

]