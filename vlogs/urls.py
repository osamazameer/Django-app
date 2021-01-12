from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='vlog-home' ),
    path('about', views.about, name='vlog-about' ),
    path('login', views.login, name='vlog-login' ),

]
