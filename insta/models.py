from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follower = models.ManyToManyField('insta.Profile', blank=True,
                                      related_name='flwer')
    following = models.ManyToManyField('insta.Profile', blank=True,
                                       related_name='flwing')

    def __str__(self):
        return self.user.username


class Post(models.Model):
    created = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=1000, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post', blank=True, null=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)

    def __str__(self):
        return self.caption
