from django.db import models
# Create your models here.

from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
import misaka

from django.contrib.auth import get_user_model

User = get_user_model()

class Album(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    photo = models.ImageField(upload_to = 'albumCover/',blank=False) 
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    likes = models.ManyToManyField(User,through="AlbumLike")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("albums:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]


class AlbumLike(models.Model):
    album = models.ForeignKey(Album, related_name="likeUnlike",on_delete=models.PROTECT)
    user = models.ForeignKey(User,related_name='user_albums',on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("album", "user")
