from django.urls import path

from . import views

urlpatterns = [
  path('', views.main),
  path('blogs/', views.ListBlogsView.as_view(), name='blogs'),
] 