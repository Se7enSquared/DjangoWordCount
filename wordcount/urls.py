from django.urls import path
from wordcount import views

urlpatterns = [
    path('', views.home),
    path('count/', views.count, name='countpage'),
    path('about/', views.about, name='aboutpage'),
    path('', views.home, name='home')
]
