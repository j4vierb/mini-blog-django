from django.contrib import admin

# Register your models here.

from .models import Blog, Blogger, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date_posted")
    list_filter = ("date_posted",)
    search_fields = ("title", "content")


class BloggerAdmin(admin.ModelAdmin):
    list_display = ("id", "bio", "user")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "content", "date_posted")
    list_filter = ("date_posted",)
    search_fields = ("content",)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Blogger, BloggerAdmin)
admin.site.register(Comment, CommentAdmin)
