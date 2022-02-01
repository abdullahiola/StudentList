from django.contrib import admin
from django.urls import path
from . import views 
from .views import register

urlpatterns = [

  path('',views.studentHome,name='studenthome'),
  path('studentlist/',views.studentList,name='studentlist'),
  path('register/',views.register,name='register'),

]
