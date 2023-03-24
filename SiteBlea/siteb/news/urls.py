from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='novosti'),
    path('<int:pk>', views.dinamicStranits.as_view(), name='newsdinamic')
]