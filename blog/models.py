from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Blog(models.Model):
  title = models.CharField(
    max_length=100,
    help_text=_('Enter the title of the blog')
  )
  content = models.TextField(help_text=_('Enter the content of the blog'))
  date_posted = models.DateTimeField(
    auto_now_add=True,
    help_text=_('Enter the date the blog was posted')
  )
  blogger = models.ForeignKey(
    'Blogger',
    related_name='blogs', # this is the related name to access blogs from blogger (no more blog_set)
    help_text=_('Select the blogger that writes this post'),
    on_delete=models.DO_NOTHING
  ) # from blogger we acces blogs using related_name

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('blog-detail', kwargs={'pk': self.pk})
  
  class Meta:
    db_table = 'blog'

class Blogger(models.Model):
  username = models.CharField(
    max_length=100,
    help_text=_('Enter the username of the blogger')
  )
  email = models.EmailField(help_text=_('Enter the email of the blogger'))
  bio = models.TextField(
    help_text=_('Enter the bio of the blogger'),
    blank=True
  )

  def __str__(self):
    return self.username
  
  def get_absolute_url(self):
    return reverse('blogger-detail', kwargs={'pk': self.pk})
  
  class Meta:
    db_table = 'blogger'

class Comment(models.Model):
  content = models.TextField(
    help_text=_('Enter the content of the comment')
  )
  blog = models.ForeignKey(
    Blog,
    related_name='comments',
    help_text=_('Select the blog that this comment belongs to'),
    on_delete=models.CASCADE
  )
  blogger = models.ForeignKey(
    'Blogger',
    related_name='comment',
    help_text=_('Select the author of the comment'),
    on_delete=models.DO_NOTHING # when Blogger is deleted, the comment remains
  )
  date_posted = models.DateTimeField(
    auto_now_add=True,
    help_text=_('Enter the date the comment was posted')
  )

  def __str__(self):
    return f'{self.content[:20]}...'
  
  class Meta:
    db_table = 'comment'
