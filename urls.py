from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index),
    path('next', views.process),
    path('reset', views.reset)
]