from django.urls import path

from .views import IndexListView, PostUpdateView, ContactUpdateView, PostListView, PostCreateView, MessageListView, MessageDetailView, MessageUpdateView

app_name = 'setup'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('edit/post/<slug:slug>', PostUpdateView.as_view(), name='edit-post'),
    path('post/add/', PostCreateView.as_view(), name='create-post'),
    path('post/', PostListView.as_view(), name='post'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='message-update'),
    path('message/detail/<int:pk>', MessageDetailView.as_view(), name='message-detail'),
    path('message/', MessageListView.as_view(), name='messages'),
    path('edit/contact/<int:pk>', ContactUpdateView.as_view(), name='edit-contact'),
]