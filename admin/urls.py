from django.conf.urls import patterns, url

from . import views

__autor__ = "Angel"

urlpatterns = [#'admin.views',
            url(r'^$', views.login_view, name='login'),
            url(r'^logout/$', views.logout_view, name='logout'),
]