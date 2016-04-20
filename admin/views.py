#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from users.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import sys


__author__ = 'Angel'


def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated() and request.user.is_superuser:
            return HttpResponseRedirect('/admin/users/')

        msg = None
        ctx = {'msg': msg}
        if 'next' in request.GET:
            ctx['next'] = request.GET['next']

        return render_to_response('admin/login.html', ctx, context_instance=RequestContext(request))
    else:
        msg = None

        if request.user.is_authenticated():
            if not request.user.is_superuser or not request.user.is_staff:
                logout(request)
            else:
                return redirect("user_list")
        if 1==1:
            username = request.POST['username']
            password = request.POST['password']

            try:
                user = User.objects.get(username=username)
                if user.is_active:
                    if user.is_superuser or user.is_staff:
                        if user.check_password(password):
                            user = authenticate(username=username, password=password)
                            request.session.set_expiry(3600000)     # 1 hour
                            login(request, user)

                            if 'next' in request.POST:
                                return HttpResponseRedirect(request.POST['next'])

                            return HttpResponseRedirect('/admin/user_list')
                        else:
                            msg = "Usuario o contraseña incorrecto"
                    else:
                        msg = "Usuario no autorizado para esta aplicación"
                else:
                    msg = "Usuario desactivado"
            except User.DoesNotExist:
                msg = "Usuario o contraseña incorrecto"
                log.error(" Unknown error: %s" % username)
            except:
                msg = "Error no contemplado"
                log.error(" Unknown error: %s" % sys.exc_value)

            ctx = {'msg': msg, 'page': 'ag'}
            return render_to_response("admin/login.html", ctx, context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home')




"""
def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated() and request.user.is_superuser:
            return HttpResponseRedirect('/admin/users/')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('admin/users/')# Redirect to a success page.
            else:
                return HttpResponseRedirect('/home')# Return a 'disabled account' error message
        else:
            return HttpResponseRedirect('/home')# Return an 'invalid login' error message.


@login_required
def logout_view(request):
    logout(request)
    #return HttpResponseRedirect('/admin/')
    return render_to_response("home/index.html")
"""