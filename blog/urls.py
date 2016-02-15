from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^beacons/$', views.beacon_list, name='beacon_list'),
    url(r'^sessions/$', views.session_list, name='session_list'),
]