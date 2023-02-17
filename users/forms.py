from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_image', 'email']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control shadow-none rounded-1 border-0 text-white border-secondary bg-dark'})

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control shadow-none rounded-1 border-0 text-white border-secondary bg-dark'})