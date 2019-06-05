from django.urls import path
from .views import signup_view, login_view, logout_view, profile_view, profile_update
from django.contrib.auth import views as auth_views


app_name = 'user'
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_update, name='profile_update'),
]
