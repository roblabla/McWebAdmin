# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.context import RequestContext


@login_required()
def index(request):
    thepage = RequestContext(request, {
        #'username': request,
        'username': "hi",
    })
    return render(request,"dashboard.html",thepage)