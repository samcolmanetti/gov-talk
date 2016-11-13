from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.registerUser, name="registerUser"),
    url(r'^newuser/', views.newUserAddress, name="newUserAddress"),
]