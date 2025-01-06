from django.urls import path

from . import views

urlpatterns = [
  path('', views.main, name='blog'),
  path('blogs/', views.BlogListView.as_view(), name='blogs'),
  path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
  path('bloggers/<int:pk>/', views.BloggerDetailView.as_view(), name='blogger-detail'),
]
