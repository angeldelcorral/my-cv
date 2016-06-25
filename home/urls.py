from django.conf.urls import patterns, url
from home import views
__autor__ = "Angel"

urlpatterns = [#'home.views',
			url(r'^$', views.index_view, name='index'),
			]