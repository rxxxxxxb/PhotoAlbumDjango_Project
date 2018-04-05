from django.conf import settings
from django.urls import reverse
from django.db import models

import misaka

from albums.models import Album

from django.contrib.auth import get_user_model
User = get_user_model()


class Photo(models.Model):
    user = models.ForeignKey(User, related_name="photos",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to = 'photos/',blank=False,unique=True) 
    message = models.TextField()
    message_html = models.TextField(editable=False)
    album = models.ForeignKey(Album, related_name="photos",null=True, blank=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "photos:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
