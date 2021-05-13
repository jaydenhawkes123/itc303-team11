from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='cloud-lab-home'),
    path('templateBuilder/', views.templateBuilder,
         name='cloud-lab-template-builder'),
    path('about/', views.about, name='cloud-lab-about'),
]

urlpatterns += staticfiles_urlpatterns()
