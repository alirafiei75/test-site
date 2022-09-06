from django import forms
from website.models import Contact

class ContactForm(forms.ModelForm):

    subject = forms.CharField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'