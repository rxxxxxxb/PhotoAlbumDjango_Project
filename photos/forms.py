from django import forms

from photos import models


class PhotoForm(forms.ModelForm):
    class Meta:
        fields = ("message", "album",'photo')
        model = models.Photo

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["album"].queryset = (
                models.Album.objects.filter(
                    pk__in=user.albums.values_list("album__pk")
                )
            )
