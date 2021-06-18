from django import forms
from .models import Company
from django.core.validators import RegexValidator


class CompanyForm(forms.ModelForm):
    name = forms.CharField(min_length=5, max_length=50)
    gst_number = forms.CharField(max_length=20, validators=[RegexValidator(
        '\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}', message="Enter a Valid Indian GST Number")])
    contact_number = forms.CharField(max_length=15, validators=[RegexValidator(
        '^(?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[789]\d{9}|(\d[ -]?){10}\d$', message="Enter a Valid Indian Phone Number")])

    class Meta:
        model = Company
        fields = "__all__"
        
