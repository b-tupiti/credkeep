from django.db import models
from users.models import Profile
# from .utils import encrypt_data, decrypt_data
import uuid

class PasswordField(models.BinaryField):
    description = "Encrypted password value" 
   
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 255
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)  


    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        del kwargs["blank"]
        del kwargs["null"]
        return name, path, args, kwargs  
    
    def get_prep_value(self, value):
        #encrypt data with your own function
        # return encrypt_data(value) 
        pass
  
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        print('db_value')
        # return decrypt_data(value)  
        return value
    
    def to_python(self, value):
        if isinstance(value, Credential):
            return value
        if value is None:
            return value
        #decrypt data with your own function
        print('to_python')
        # return decrypt_data(value)
        return value

class Credential(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    credential_for = models.CharField(max_length=200)
    featured_image = models.ImageField(blank=True,null=True, upload_to='accounts/', default="accounts/default.jpg")
    description = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    url = models.CharField(max_length=1250,null=True,blank=True)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.credential_for

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    class Meta:
        ordering = ['credential_for']


    