# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext
import psutil


@login_required()
def index(request):
    thepage = RequestContext(request, {
    })

    return render(request,"dashboard.html",thepage)

def mcutils(request):
    """
    mcutils view, to get ram/cpu usage, and mc related stuff.
    """
    if request.POST:
        action = request.POST.get('action')
        if action == "getram":
            return HttpResponse(psutil.phymem_usage().percent)
        elif action == "getcpu":
            return HttpResponse(psutil.cpu_percent())
    else:
        pass;