from django.conf.urls import url

from . import views

# Put URL Patterns here

app_name = 'forum'
urlpatterns = [
    url(r'^', views.index, name='index'),
]
