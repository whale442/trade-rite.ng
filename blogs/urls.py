from django.urls import path

from .import views
from .views import ( UserPostListView,PostDetailView)


urlpatterns = [
    path('',views.blog,name='blog'),
    path('user/<str:username>/', UserPostListView.as_view(),name='user-blogs'),
    path('post/<slug>/', PostDetailView.as_view(),name='post-detail'),
]