from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.
class User(models.Model) :
    user_email = models.EmailField(unique=True)
    user_pwd = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)


class Text(models.Model):
    content = models.TextField(max_length=400)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    regdate = models.DateField(default=timezone.now)

# class Post(models.Model):
#     content = models.TextField(max_length=400)
#     user_name = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_name', db_column='user_name')
#     regdate = models.DateField(default=timezone.now)
#     mainphoto = models.ImageField(blank=True, null=True)


class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name=User),
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'timeline_photo/%Y/%m/%d')
    created = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __Str__(self):
        return "text : " + self.text
    class Meta:
        ordering = ['-created']


class Avatar(models.Model):
    image = models.ImageField(blank=True, null=True)

# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     # User모델과 Profile을 1:1로 연결
#     description = models.TextField(blank=True)
#     nickname = models.CharField(max_length=40, blank=True)
#     image = models.ImageField(blank=True)
