from django.urls import path
from . import views

urlpatterns = [
    path('', views.CoinsManager.as_view(), name='glavnaea'),
    path('<int:pk>', views.strdin.as_view(), name='dinamic')
]
