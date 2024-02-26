from django.shortcuts import get_object_or_404, render
from django.utils.timezone import now

from blog.models import Category, Post
from . import const


def filter_pub_post(postmanager):
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
    post_list = filter_pub_post(Post.objects)[:const.POSTS_ON_PAGE]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        filter_pub_post(Post.objects),
        pk=post_id,
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = filter_pub_post(category.posts)
    return render(
        request,
        'blog/category.html',
        {
            'post_list': post_list,
            'category': category
        }
    )
