from django import forms
from website.models import Contact
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    subject = forms.CharField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'