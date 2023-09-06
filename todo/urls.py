from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('<int:todo_id>/', views.read),
    path('delete/<int:todo_id>/', views.delete),
    path('update/<int:todo_id>/', views.update),
]
