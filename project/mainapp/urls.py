from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.interest),
    path('submit/', views.submit),
]