
from django.urls import path,re_path
from .views import *

app_name='post'

urlpatterns = [
    path('index/',index_view,name='index'),
    path('create/',create_view,name='create'),
    re_path(r'^(?P<id>\d+)/delete/$',delete_view,name='delete'),
    re_path(r'^(?P<id>\d+)/update/$',update_view,name='update'),
    re_path(r'^(?P<id>\d+)/$',detail_view,name='detail')
]