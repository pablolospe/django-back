from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('saludar', views.saludar, name='saludar'),
    path('lista', views.lista, name='lista'),
    path('form', views.form, name='form'),
]