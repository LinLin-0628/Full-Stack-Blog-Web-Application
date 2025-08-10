from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.urls.base import reverse_lazy
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from django.http.response import JsonResponse
from django.db.models import Q

from .models import *
from .forms import *

# Create your views here.

def index(request):

    blogs = Blog.objects.all().order_by("-created_time")

    return render(request, "blog/index.html", {
        "blogs":blogs
    })


def blog_detail(request, blog_id):

    try:
        blog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        blog = None

    return render(request, "blog/blog_detail.html", {
        "blog": blog
    })

@login_required(login_url=reverse_lazy("appauth:login"))
@require_http_methods(["GET", "POST"])
def create_blog(request):

    if request.method == "GET":
        categories = BlogCategory.objects.all()

        return render(request, "blog/create_blog.html", {
            "categories": categories,
        })

    else:
        form = CreateBlogForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            category_id = form.cleaned_data.get("category")

            category = BlogCategory.objects.get(id=category_id)

            blog = Blog.objects.create(
                title=title,
                content=content,
                category=category,
                author=request.user
            )

            return JsonResponse({
                "code": 200,
                "message": "successfully created blog",
                "data": {
                    "blog_id": blog.id
                }
            }, status=200)

        else:
            print(form.errors)
            return JsonResponse({
                "code": 400,
                "message": "form invalid",
            }, status=400)



@login_required()
@require_POST
def comment(request):

    blog_id = request.POST.get("blog_id")
    comment_content = request.POST.get("content")

    BlogComment.objects.create(
        content=comment_content,
        blog_id=blog_id,
        author=request.user
    )

    return redirect(reverse("blog:blog_detail", kwargs={"blog_id":blog_id}))


@require_GET
def search(request):
    q = request.GET.get("q")

    blogs = Blog.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))

    return render(request, "blog/index.html", {
        "blogs": blogs
    })
