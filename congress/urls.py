from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/', views.display_congressmen, name="display_congressmen"),
    url(r'^register/', views.registerUser, name="registerUser"),
    url(r'^newuser/', views.newUserAddress, name="newUserAddress"),
    url(r'^login/', views.loginUser, name="loginUser"),
    url(r'^logout/', views.logoutUser, name="logoutUser"),
    url(r'^', views.index, name='index'),
]