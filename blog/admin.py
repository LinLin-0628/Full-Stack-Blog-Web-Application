from django.contrib import admin
from .models import *

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]




class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_time", "category", "author"]

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ["content", "created_time", "author", "blog"]


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)