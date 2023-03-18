from django.urls import path
from . import views

from .views import About, Product, Project, Event, Index, ContactView, ProductDetail

urlpatterns = [
    path('user/', views.admin , name='user-admin'),
    path('about/', About.as_view() , name='about'),
    path('product/', Product.as_view() , name='product'),
    path('project/', Project.as_view() , name='project'),
    path('event/', Event.as_view() , name='event'),
    path('contact/', ContactView.as_view() , name='contact'),
    path('product/<slug:slug>', ProductDetail.as_view(), name = 'detail'),
    path('', Index.as_view() , name='index'),

]
