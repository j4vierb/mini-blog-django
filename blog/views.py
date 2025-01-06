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
  paginate_by = 5

# TODO: Section of comments.
# TODO: Comments should to be order by date_posted (oldest first).
class BlogDetailView(DetailView):
  model = Blog
  template_name = 'blogs/detail.html'
  context_object_name = 'blog'

class BloggerDetailView(DetailView):
  model = Blogger
  template_name = 'bloggers/detail.html'
  context_object_name = 'blogger'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['blogs'] = Blog.objects.filter(blogger_id=self.kwargs['pk']).order_by('-date_posted')

    return context
