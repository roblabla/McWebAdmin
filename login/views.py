# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.template import RequestContext
from django.template.base import Template

def index(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("yes")
            else:
                return HttpResponse("not active")
        else:
            return HttpResponse("no")
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard/')
        else:
            thepage = RequestContext(request)
            return render(request,"login.html",thepage)
