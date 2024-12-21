from django.db import models
from hashlib import sha256
import json
# Create your models here.


class Music(models.Model):
    title = models.CharField(max_length=30, default='No title')
    writer = models.CharField(max_length=30, default='No writer')
    cover = models.FileField(default=None, upload_to='covers')
    file = models.FileField(default=None, upload_to='music')

    def __str__(self):
        return self.title


def make_password(string):
    return sha256(str(string + "Hjkdskb").encode()).hexdigest()


class Account(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=500)
    favorite_music = models.CharField(max_length=500, default='', null=True)

    def set_music(x):
        return json.dumps(x)

    def get_music(x):
        if x == '':
            return []
        return json.loads(x)

    def __str__(self):
        return self.username


