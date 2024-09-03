from django import forms
from .models import Person
from django.core.validators import RegexValidator


class PersonForm(forms.ModelForm):
    class Meta:
    #     phone_number = forms.CharField(
    #     max_length=15,
    #     validators=[RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be between 9 and 15 digits.")]
    # )
        model = Person
        fields = ('name', 'phone_number', 'email', 'address', 'last_name','speciality',)
        
