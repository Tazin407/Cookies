from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    # path("", views.SetCookie, name='set_cookie'),
    path("", views.SetSession, name='set_cookie'),
    # path("get_cookie/", views.GetCookie, name='get_cookie'),
    path("get_cookie/", views.GetSession, name='get_cookie'),
    # path("del_cookie/", views.DeleteCookie, name='del_cookie'),
    path("del_cookie/", views.del_session, name='del_cookie'),
    
]