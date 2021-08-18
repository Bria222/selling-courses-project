from django.urls import  path
from django.http import HttpResponse
from django.contrib import admin
from . import views


urlpatterns = [
    path( '', views.home,name='home'),
    path( 'contact/', views.contact,name='contact'),
    path( 'about/', views.about,name='about'),
    path( 'projects/', views.projects,name='projects'),
    path( 'createProject/', views.createProject,name='create-project'),
    path( 'updateProject', views.updateProject,name='update-project'),
]