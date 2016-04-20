from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response


# Create your views here.
from django.template import RequestContext

from users.models import UserProfile

def user_list(request):
    user = User.objects.filter()
    return render_to_response("admin/users/index.html", locals(), context_instance=RequestContext(request))

def edit_user(request, user_id=None):
    if request.method == 'GET':
        user = User.objects.get(id=user_id)
        return render_to_response('admin/users/edit_user.html', {'u':user,}, context_instance=RequestContext(request))

    else:
        id = request.POST['id']
        user = User.objects.get(pk=id)
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()

        if UserProfile.objects.filter(user=user).count()>0:
            user_profile = UserProfile.objects.get(user=user)
        else:
            user_profile = UserProfile.objects.create(user=user)

        if 'first_name' in request.POST:
            user_profile.first_name = request.POST['first_name']
        if 'last_name' in request.POST:
            user_profile.last_name = request.POST['last_name']
        if 'address' in request.POST:
            user_profile.address = request.POST['address']
        if 'cel_phone' in request.POST:
            user_profile.cel_phone = request.POST['cel_phone']
        if 'phone' in request.POST:
            user_profile.phone = request.POST['phone']
        if 'user' in request.POST:
            user_profile.user = request.POST['user']
        if 'birthdate' in request.POST:
            user_profile.birthdate = request.POST['birthdate']

        user_profile.save()

    return HttpResponseRedirect("/admin/users/")