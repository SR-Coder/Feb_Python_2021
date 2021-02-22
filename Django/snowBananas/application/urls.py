from django.urls import path
from . import views

urlpatterns = [
    path('', views.dispLogin),
    path('dashboard', views.dispDashboard),
    path('guest/<str:name>', views.dispGuest),
    path('create', views.dispCreate),




    # ACTION ROUTES
    path('login', views.login),
    path('logout', views.logout),
    path('newUser', views.newUser),
    path('create/newNanna', views.createNewNanna),
    path('like/<int:nannaID>', views.likeANanna),

]