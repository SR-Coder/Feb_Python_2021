from django.urls import path
from . import views

urlpatterns = [
    #display path
    path('', views.dispLogin), # this displays the login page that has my forms on it
    path('success', views.dipsSuccess),

    #action paths
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
]
