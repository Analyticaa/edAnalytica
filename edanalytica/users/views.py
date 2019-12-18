from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView as AuthLoginView

def index(request, *args, **kwargs):
    return HttpResponseRedirect('/s/login/')


class UserLoginView(AuthLoginView):
    template_name = 'users/login.html'