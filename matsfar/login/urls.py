from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sum',views.sum, name='sum'),
     path('rectangle',views.rectangle, name='rectangle'),
     path('square',views.square, name='square'),
     path('circle',views.circle, name='circle'),
     path('index', views.index, name='index'),
]