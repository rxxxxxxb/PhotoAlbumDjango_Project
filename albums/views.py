from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)

from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from albums.models import Album
from albums.models import AlbumLike
from . import models



class CreateAlbum(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description","photo")
    model = Album

class SingleAlbum(generic.DetailView):
    model = Album

class ListAlbums(generic.ListView):
    model = Album


class LikeAlbum(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("albums:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        album = get_object_or_404(Album,slug=self.kwargs.get("slug"))

        try:
            AlbumLike.objects.create(user=self.request.user,album=album)

        except IntegrityError:
            messages.warning(self.request,("Warning, already liked  {}".format(album.name)))

        else:
            messages.success(self.request,"Liked {} album.".format(album.name))

        return super().get(request, *args, **kwargs)


class UnlikeAlbum(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("albums:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            likeUnlike = models.AlbumLike.objects.filter(
                user=self.request.user,
                album__slug=self.kwargs.get("slug")
            ).get()

        except models.AlbumLike.DoesNotExist:
            messages.warning(
                self.request,
                "You can't Unlike this album because you already did."
            )
        else:
           likeUnlike.delete()
           messages.success(
                self.request,
                "You have unliked this album."
            )
        return super().get(request, *args, **kwargs)
