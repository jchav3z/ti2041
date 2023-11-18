from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'Post': post})


def post_details(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'myblog/post_detail.html', {'post': post})


def category_posts(request, category_id):
    category = get_object_or_404(category, pk = category_id)
    posts = Post.objects.filter(category = category).select_related('author', 'category')
    return render(request, 'myblog/categoty_posts.html', {'category': category, 'posts': posts})


def tag_posts(request, tag_id):
    tag = get_object_or_404(tag, pk = tag_id)
    posts = Post.objects.filter(tags = tag).select_related('author', 'category')
    return render(request, 'myblog/tag_posts.html', {'tag': tag, 'posts': posts})