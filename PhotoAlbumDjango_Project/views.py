from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html' #after logging in: test.html is loaded

class ThanksPage(TemplateView):
    template_name = 'thanks.html' #after logging out: thanks.html is loaded

class HomePage(TemplateView):
    template_name = "index.html" #default Homepage : index.html 

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test")) #after logging in : reversed to test.html
        return super().get(request, *args, **kwargs)
