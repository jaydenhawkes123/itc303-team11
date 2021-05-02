from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cloud-lab-home'),
    path('about/', views.about, name='cloud-lab-about'),
]
