from django.shortcuts import get_object_or_404, render
from blog.models import Post, Category
from datetime import datetime


def index(request):
    post_list = Post.objects.select_related(
    ).filter(
        pub_date__lt=datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        pk=post_id,
        pub_date__lt=datetime.now(),
        is_published=True,
        category__is_published=True)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    post_list = Post.objects.select_related(
    ).filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lt=datetime.now()
    ).order_by('-pub_date')
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    context = {
        'post_list': post_list,
        'category': category

    }
    return render(request, 'blog/category.html', context)
