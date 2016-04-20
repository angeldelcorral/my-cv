from django.conf.urls import patterns, url

from . import views

__autor__ = "Angel"

urlpatterns = [#'admin.views',
            url(r'^$', views.login_view, name='login'),
            url(r'^logout/$', views.logout_view, name='logout'),

                #url(regex=r'^$', view=views.login_view, name='login'),
                #url(regex=r'^logout/$', view=views.logout_view, name='logout'),

                    #url(r'^$', 'login_view', name='login'),
                    #url(r'^logout/$', 'logout_view', name='logout'),
]