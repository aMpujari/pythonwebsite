from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about,name='about us'),
    url(r'^welcome/$',views.welcome,name='wadakam'),
    url(r'^new_user$',views.create,name='form submission'),      
      url(r'^message/$',views.msg,name='msg'),
]
