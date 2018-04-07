from django.conf.urls import url

from . import views

app_name='photos'

urlpatterns = [
    #home view for photos
    url(r"^$", views.PhotoList.as_view(), name="all"),
    
    #Posting New  photo
    url(r"new/$", views.CreatePhoto.as_view(), name="create"),
    
    #individual user photo view
    url(r"by/(?P<username>[-\w]+)/$",views.UserPhotos.as_view(),name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PhotoDetail.as_view(),name="single"),
    
    #Delete photo
    url(r"delete/(?P<pk>\d+)/$",views.DeletePhoto.as_view(),name="delete"),
]
