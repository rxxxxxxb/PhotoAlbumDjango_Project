from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'albums'

urlpatterns = [
    url(r"^$", views.ListAlbums.as_view(), name="all"), #Album Homepage

    url(r"^new/$", views.CreateAlbum.as_view(), name="create"), # Creating new album
    url(r"^photos/in/(?P<slug>[-\w]+)/$",views.SingleAlbum.as_view(),name="single"), # individual Photos
    url(r"likeAlbum/(?P<slug>[-\w]+)/$",views.LikeAlbum.as_view(),name="like"), #Like Photo
    url(r"unlike/(?P<slug>[-\w]+)/$",views.UnlikeAlbum.as_view(),name="unlike"), #unlike photo
]
