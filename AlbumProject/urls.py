"""AlbumProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^accounts/", include("accounts.urls", namespace="accounts")), #redirect to accounts urls file
    url(r"^accounts/", include("django.contrib.auth.urls")), #django package for user authentications
    
    url(r"^albums/",include("albums.urls", namespace="albums")),#redirect to albums urls file
    url(r"^photos/", include("photos.urls", namespace="photos")),#redirect to Photos urls file


    url(r"^$", views.HomePage.as_view(), name="home"),#Homepage : default


    url(r"^test/$", views.TestPage.as_view(), name="test"), # Homepage : after Logging in
    url(r"^thanks/$", views.ThanksPage.as_view(), name="thanks"), # after Logout View


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #for media files: albumCover and photos.

