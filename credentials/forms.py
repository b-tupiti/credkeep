from django.forms import ModelForm
from django import forms
from .models import Credential

class CredentialForm(ModelForm):
    class Meta:
        model = Credential
        fields = ['credential_for', 'url', 'featured_image', 'description', 'username', 'password']
        widgets = {
          'description': forms.Textarea(attrs={'rows':2,}),
        }
    
    def __init__(self, *args, **kwargs):
        super(CredentialForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control shadow-none rounded-1 border-0 text-white border-secondary bg-dark'})
    
    