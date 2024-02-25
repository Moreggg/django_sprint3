from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from blog.models import Category, Post
from . import const


def filt_func(postmanager):
    return postmanager.select_related(
        'author',
        'location',
        'category',
    ).filter(
        pub_date__lt=now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    post_list = filt_func(Post.objects)[:const.SLICE]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        filt_func(Post.objects),
        pk=post_id,
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    post_list = filt_func(Category.objects.get(slug=category_slug).posts)
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    return render(
        request,
        'blog/category.html',
        {
            'post_list': post_list,
            'category': category
        }
    )
