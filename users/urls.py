from django.conf.urls import patterns, url

from users import views

urlpatterns = [#'users.views',
			   url(r'^$', views.user_list, name='user_list'),
			   #url(regex=r'^$', view=views.user_list, name='user_list'),
					#url(r'^$', 'user_list', name='user_list'),
]