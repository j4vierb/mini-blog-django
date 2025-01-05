from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def main(request):
  return render(request, 'blog/index.html')

from .models import Blog

class ListBlogsView(ListView):
  model = Blog
  template_name = 'blogs/list-blogs.html'
  context_object_name = 'blogs'
