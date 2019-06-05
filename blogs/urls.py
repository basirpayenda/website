from django.urls import path, include
from . import views as blogs_view


app_name = 'blog'
urlpatterns = [
    path('', blogs_view.home, name='home'),
    path('blogs/', blogs_view.blogs, name='blogs'),
    path('<slug:blog_slug>', blogs_view.blog_detail, name='blog_detail'),
    path('post/', blogs_view.blog_create, name='blog_create'),
    path('<slug:blog_slug>/edit/', blogs_view.blog_update, name='blog_update'),
    path('<slug:blog_slug>/delete/', blogs_view.blog_delete, name='blog_delete'),
    path('search-posts/', blogs_view.search_view, name='search_blogs'),
    path('blogs/<author>/', blogs_view.user_profile, name='user_post'),
    path('tinymce/', include('tinymce.urls')),
    path('category/<slug:category_name>/', blogs_view.category_blogs, name='category_blogs'),
]
