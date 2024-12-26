from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.template.defaultfilters import slugify
import os
class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Users", self.username, instance)
        return None



    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, default='regular')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    image = models.ImageField(default='default/user.jpg', upload_to=image_upload_to)

    def __str__(self):
        return self.username


class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.slug), instance)
        return None

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True) 
    slug = models.SlugField("Sheik slug", null=False, blank=False, unique=True)
    published = models.DateTimeField("Date published", default=timezone.now)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']

class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.series.slug), slugify(self.article_slug), instance)
        return None
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    article_slug = models.SlugField("gategory slug", null=False, blank=False, unique=True)
    image=models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)
    content = HTMLField(blank=True, default="")
    notes = HTMLField(blank=True, default="")
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default="", verbose_name="sheik", on_delete=models.SET_DEFAULT)
    author = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT, related_name="article_author")
    
    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']

class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
class order(models.Model):
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='', max_length=100)
    phonenumber=models.IntegerField("Phone Number")
    created_date = models.DateTimeField('Date created', default=timezone.now)
    def __str__(self):
        return f"{self.name},{self.phonenumber}"
class Fatwa(models.Model):
    name=models.CharField(max_length=100,default='')
    question = models.TextField()  
    answer = models.TextField()    
    date = models.DateTimeField(auto_now_add=True)  
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Fatwa {self.id} - {self.category if self.category else 'General'}"
    

class WallEntry(models.Model):
    wall_number = models.CharField(max_length=100)
    screenshot = models.ImageField(upload_to='screenshots')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_filled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" username: {self.user} - wallet: {self.wall_number} - date: {self.date_filled.strftime('%Y-%m-%d %H:%M')}"