from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        #loads above fields for registration 
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Display username as Display Name  
        self.fields["username"].label = "Display name"      
        # Display email as Email Address
        self.fields["email"].label = "Email address" 