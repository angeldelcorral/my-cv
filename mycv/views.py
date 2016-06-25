from django.http import HttpResponseRedirect

__autor__ = "Angel"

def home(request):
    return HttpResponseRedirect("/home")