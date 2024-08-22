from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_url, name='create_url'),
    path('create/', views.createpage, name='createpage'),
    path('<code>/', views.redirect_url, name='redirect_url'),
]