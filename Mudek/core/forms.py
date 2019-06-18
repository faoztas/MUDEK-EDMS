# Django
from django import forms
from django.core.mail import send_mail
from django.utils.translation import ugettext as _

# Local Django
from .models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(label=_("First Name"),
        widget=forms.TextInput(
            attrs=dict({'class': 'form-control'})),
            required=True
    )
    last_name = forms.CharField(label=_("Last Name"),
        widget=forms.TextInput(
            attrs=dict({'class': 'form-control'})),
            required=True
    )
    email = forms.EmailField(label=_("Email"),
        widget=forms.TextInput(
            attrs=dict({'class': 'form-control'})),
            required=True
    )
    message = forms.CharField(label=_("Message"),
        widget=forms.Textarea(
            attrs={'rows': '4', 'class': 'form-control'}
        )
    )
   
    def send_mail(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        emailTo = ['mudekedms@gmail.com']
     
    class Meta:
        model = Contact
        exclude = ('admin_read', )