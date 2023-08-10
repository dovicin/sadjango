from django import http, views
from django.urls import path
from . import views

#http://127.0.0.1:8000/         => homepage
#http://127.0.0.1:8000/index    => homepage
#http://127.0.0.1:8000/about    => aboutpage
#http://127.0.0.1:8000/contact  => contact
#http://127.0.0.1:8000/signup  => sign up page
#http://127.0.0.1:8000/blogs    => blogs
#http://127.0.0.1:8000/blogs/3  => blog-details

urlpatterns = [
    path("", views.join_form),
    #path("signup", views.signup),
    path("signup.html", views.join_form, name='signup.html'),
     path("success.html", views.success, name='success.html'),
]