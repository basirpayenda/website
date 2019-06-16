from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from marketing.forms import EmailSignupForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User



def get_category_count():
    queryset = Blog \
        .objects \
        .values('category__title') \
        .annotate(Count('category__title'))
    return queryset


def home(request):
    subscribe_form = EmailSignupForm()
    queryset = Blog.objects.filter(featured=True).order_by('-created_at')
    latest = Blog.objects.filter(blog_views__gte=5)
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 5)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs': blogs,
        'latest': latest,
        'title':'home',
        'subscribe_form' : subscribe_form,
        'categories': get_category_count()
        # 'views': blog_view_num
    }
    return render(request, 'blogs/home.html', context)


def blogs(request):
    subscribe_form = EmailSignupForm()
    queryset = Blog.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 4)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs':blogs,
        'title':'blogs list',
        'subscribe_form': subscribe_form,
        'categories': get_category_count()
    }
    return render(request, 'blogs/blogs.html', context)


def blog_detail(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    session_key = 'blog_views_{}'.format(blog.slug)
    if not request.session.get(session_key):
        blog.blog_views += 1
        blog.save()
        request.session[session_key] = True

    context = {
        'blog': blog,
        'categories': get_category_count()
    }

    return render(request, 'blogs/blog-detail.html', context)


@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            slug = form.instance.slug
            form.save()
            return redirect('/')
    form = BlogForm()
    context = {
        'form':form,
        'categories': get_category_count()
    }
    return render(request, 'blogs/form.html', context)


@login_required
def blog_update(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    # if not request.user == blog.author:  # or
    if not request.user.username == blog.author.username:  # or
        print(request.user)  # basirpayenda (current logged in user)
        print(request.user.username) # basirpayenda
        print(blog.author)  # admin
        print(blog.author.username) # admin
        raise PermissionDenied

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/')

    form = BlogForm(instance=blog)
    title = blog.title
    context= {
        'form': form,
        'form_data': title,
        'categories': get_category_count()
    }
    return render(request, 'blogs/update-form.html', context)


@login_required
def blog_delete(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    if not request.user == blog.author:
        raise PermissionDenied

    if request.method == 'POST':
        blog.delete()
        return redirect('/')

    context = {
        'blog':blog,
        'categories': get_category_count()
    }
    return render(request, 'blogs/blog-delete.html', {'blog':blog})


def search_view(request):
    queryset = Blog.objects.all()
    q = request.GET.get('q')

    if q:
        queryset = queryset.filter(Q(title__icontains=q)|Q(overview__icontains=q))

    context = {
        'results':queryset,
        'query':q,
        'categories': get_category_count()
    }
    return render(request, 'blogs/search-results.html', context)


def user_profile(request, author):
    user = get_object_or_404(User, username=author)
    queryset = Blog.objects.filter(author=user).order_by('-created_at')
    print(queryset)
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page', 1)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs' : blogs,
        'author' : user,
        'categories': get_category_count()
    }
    return render(request, 'blogs/user-posts.html',context)


def category_blogs(request, category_name):
    subscribe_form = EmailSignupForm()
    queryset = Blog.objects.filter(category__title = category_name).order_by('-created_at')
    paginator = Paginator(queryset, 5)
    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs': blogs,
        'categories':get_category_count(),
        'subscribe_form': subscribe_form,
        'categories': get_category_count()

    }
    return render(request, 'blogs/category-blogs.html', context)