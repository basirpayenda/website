from django.urls import path
from .views import contact, success

app_name='contact'
urlpatterns = [
    path('contact/', contact, name='contact'),
    path('mail-sent/success/', success, name='success'),
]
