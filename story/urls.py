from django.conf.urls import url

from . import views

app_name = 'story'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<story_id>[0-9]+)/$', views.story, name='story'),
]