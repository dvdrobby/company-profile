from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.admin , name='user-admin'),
    path('post/', views.post , name='post'),
    path('contact/', views.contact , name='contact'),
    path('', views.index , name='index'),

]
