from django.shortcuts import render_to_response
from django.template.context import RequestContext
from users.models import User


def index_view(request):
	user = User.objects.get()
	user_profile = User.objects.filter(id=1)
	return render_to_response('home/index.html', locals(), context_instance=RequestContext(request))