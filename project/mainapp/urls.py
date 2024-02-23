from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url= 'interest/')),
    path('interest/', views.interest),
    path('interest/submit/', views.submit_interest),
    path('aptitude/', views.aptitude),
]