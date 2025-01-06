from django.contrib import admin

# Register your models here.

from .models import Blog, Blogger

class BlogAdmin(admin.ModelAdmin):
  list_display = ('title', 'date_posted')
  list_filter = ('date_posted',)
  search_fields = ('title', 'content')

class BloggerAdmin(admin.ModelAdmin):
  list_display = ('username', 'email')
  search_fields = ('username', 'email')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Blogger, BloggerAdmin)
