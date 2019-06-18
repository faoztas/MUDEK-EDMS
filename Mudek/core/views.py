# Django
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.contrib import messages

# Local Django
from .forms import ContactForm
from .models import Contact

class ContactView(SuccessMessageMixin, CreateView):
    template_name = 'core/contact.html'
    model = Contact
    form_class = ContactForm
    success_url = '/lessons'
    success_message = 'Email sent successfully. Thank you.'

    def get_success_message(self, cleaned_data):
        send_mail(self.object.first_name, self.object.last_name, self.object.email, ['mudekedms@gmail.com'], fail_silently=False)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super(ContactView, self).form_valid(form)
