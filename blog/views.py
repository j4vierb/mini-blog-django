from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView

# Create your views here.
def main(request):
  return render(request, 'blog/index.html')

from .models import Blog, Blogger, Comment

class BlogListView(ListView):
  model = Blog
  template_name = 'blogs/list.html'
  context_object_name = 'blogs'
  ordering = ['-date_posted']
  paginate_by = 5

class BlogDetailView(DetailView):
  model = Blog
  template_name = 'blogs/detail.html'
  context_object_name = 'blog'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['comments'] = Comment.objects.all().filter(blog_id=self.kwargs['pk']).order_by('date_posted')
    
    return context

class BloggerListView(ListView):
  model = Blogger
  template_name = 'bloggers/list.html'
  context_object_name = 'bloggers'
  ordering = ['username']

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    return context

class BloggerDetailView(DetailView):
  model = Blogger
  template_name = 'bloggers/detail.html'
  context_object_name = 'blogger'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['blogs'] = Blog.objects.filter(blogger_id=self.kwargs['pk']).order_by('-date_posted')

    return context

class CommentEditView(UpdateView):
  model = Comment
  template_name = 'comments/edit.html'
  context_object_name = 'comment'
  fields = ['content']

  def get_success_url(self):
    """GET current blog id and redirect to blog detail page"""
    blog_id = self.kwargs['blog_id']
    return Blog.objects.get(id=blog_id).get_absolute_url()

# TODO: Logged out users will be directed to the login page to log in,
# before they can add comments. After logging in, they will be redirected
# back to the blog page they wanted to comment on.
class CommentCreateView(CreateView):
  model = Comment
  template_name = 'comments/edit.html'
  fields = ['content']

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    blog_id = self.kwargs['blog_id']
    context['blog'] = Blog.objects.all().filter(id=blog_id).first()
    context['blog_id'] = blog_id

    return context

  def form_valid(self, form):
    blog_id = self.kwargs['blog_id']
    user = self.request.user
    
    form.instance.blog = Blog.objects.get(id=blog_id)
    form.instance.blogger = Blogger.objects.get(user=user)
  
    return super().form_valid(form)
