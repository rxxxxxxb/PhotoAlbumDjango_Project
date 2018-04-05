from django.contrib import admin

# Register your models here.
from . import models


class AlbumLikeInline(admin.TabularInline):
    model = models.AlbumLike

admin.site.register(models.Album)
