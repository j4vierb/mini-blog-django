from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
def main(request):
  return render(request, 'blog/index.html')

from .models import Blog, Blogger

class BlogListView(ListView):
  model = Blog
  template_name = 'blogs/list.html'
  context_object_name = 'blogs'
  ordering = ['-date_posted']

class BlogDetailView(DetailView):
  model = Blog
  template_name = 'blogs/detail.html'
  context_object_name = 'blog'

class BloggerDetailView(DetailView):
  model = Blogger
  template_name = 'bloggers/detail.html'
  context_object_name = 'blogger'
