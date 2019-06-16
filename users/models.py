from django.db import models
from django.contrib.auth.models import User

# user, image, description, facebook, whatsapp

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    introduction = models.CharField(max_length=150, null=True, blank= True, default=f'Apparently, this user prefers to keep an air of mystery about them.')
    image = models.ImageField(default='default.jpg', upload_to='profile_pictures')
    description = models.TextField()
    facebook = models.CharField(max_length=255, blank=True)
    whatsapp = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{ self.user.username } Profile"
