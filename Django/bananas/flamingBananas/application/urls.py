from django.urls import path
from . import views

urlpatterns = [
    #DISPLAY PATHS
    path('', views.displayIndex),
    path('hello/<int:myAge>', views.helloAge),
    path('payments', views.displayPayments),
    path('success', views.displaySuccess),

    #ACTION PATHS
    path('hello/sendMeHome', views.sendHome),
    path('processCard', views.processCard),
]
