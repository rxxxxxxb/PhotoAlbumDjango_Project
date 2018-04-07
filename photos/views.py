from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models 

from django.contrib.auth import get_user_model
User = get_user_model()

#List all photo class
class PhotoList(SelectRelatedMixin, generic.ListView):
    model = models.Photo
    select_related = ("user", "album")

#Individual user photos Class
class UserPhotos(generic.ListView):
    model = models.Photo
    template_name = "photos/user_photo_list.html"

    def get_queryset(self):
        try:
            self.photo_user = User.objects.prefetch_related("photos").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.photo_user.photos.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photo_user"] = self.photo_user
        return context

#Single photo Detail class 
class PhotoDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Photo
    select_related = ("user", "album")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

#Posting/Creating a Photo post class
class CreatePhoto(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message','album','photo')
    model = models.Photo

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({"user": self.request.user})
    #     return kwargs
    
    #form validation
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

#Delete a single Class
class DeletePhoto(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Photo
    select_related = ("user", "album")
    success_url = reverse_lazy("photos:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Photo Deleted")
        return super().delete(*args, **kwargs)
