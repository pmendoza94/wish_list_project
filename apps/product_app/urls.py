from django.conf.urls import url
from . import views

def test(request):
    print '*** product_app urls ***'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^create_process$', views.create_process),
    url(r'^wish_item/(?P<product_id>\d+)$', views.wish_item),
    url(r'^add/(?P<product_id>\d+)/(?P<user_id>\d+)$', views.add),
    url(r'^remove/(?P<product_id>\d+)/(?P<user_id>\d+)$', views.remove),
    url(r'^delete/(?P<product_id>\d+)/(?P<user_id>\d+)$', views.delete),
]
