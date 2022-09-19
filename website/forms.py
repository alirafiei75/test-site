from django import forms
from website.models import Contact
from captcha.fields import CaptchaField
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    subject = forms.CharField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'


class PasswordResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']