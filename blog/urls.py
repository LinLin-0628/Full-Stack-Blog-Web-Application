from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("blog/<int:blog_id>", views.blog_detail, name="blog_detail"),
    path("create", views.create_blog, name="create_blog"),
    path("comment", views.comment, name="comment"),
    path("search", views.search, name="search")
]