from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth import logout
from django.conf import settings

def index(request, *args, **kwargs):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return HttpResponseRedirect('/s/login/')


class UserLoginView(AuthLoginView):
    template_name = 'users/login.html'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)
