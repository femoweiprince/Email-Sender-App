from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home'),
    path('Email',views.Email,name='Email')
    

    
]
