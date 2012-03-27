# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.template.base import Template

def index(request):
def validate(request):
    state = "notpost"
username = password = ''
if request.POST:
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            state="yes"
        else:
            state = "not active"
    else:
        state = "no"
thepage = RequestContext(request, {
    'state': state,
    'username': username,
    })
t = Template("login.html")
return HttpResponse(t.render(thepage))
