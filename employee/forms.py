from django import forms
from django.core.validators import MaxLengthValidator
class employeeForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email_number = forms.EmailField(max_length=150)
    password = forms.CharField(max_length=15)
    phone_number = forms.CharField(validators=[MaxLengthValidator(10)],max_length=10)
    job_title = forms.CharField(max_length=150)

class SearchForm(forms.Form):
    first_name = forms.CharField(max_length=150)