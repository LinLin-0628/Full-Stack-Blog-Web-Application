from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Blog Category
class BlogCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Blog Categories"


# Blog Posts
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.title

# Comments
class BlogComment(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.content