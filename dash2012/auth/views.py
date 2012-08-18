from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def login(r):
    if r.POST:
        username = r.POST['username']
        password = r.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(r, user)
            return HttpResponseRedirect(reverse('myaccount-view'))

    return render(r, 'auth.html')

def register(r):
    return render(r, 'index.html')

def logout(request):
    auth_logout(request)
    return render(request, 'index.html')