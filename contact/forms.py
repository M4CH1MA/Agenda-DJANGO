from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):

    picture = forms.ImageField(widget=forms.FileInput(attrs={
        'accept': 'image/*',
    }))

    class Meta:
        model = models.Contact
        fields = 'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder':'Digite seu nome',
                } 
            )
        }

        def clean(self):
            return super().clean()
        
        #def clean_first_name(self):
        #   first_name = self.cleaned_data.get('first_name')

        #   if first_name == 'ABC':
        #       self.add_error('first_name',ValidationError('Veio do add_error',code='invalid'))

        #   return first_name
    

class RegisterForm(UserCreationForm):
    ...