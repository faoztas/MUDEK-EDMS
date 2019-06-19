from django import forms
from .models import Lesson, Other_Document, Requested_Documents
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible
from django.contrib.auth import authenticate


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = [
        'lesson_content', 'lesson_content_file',
        'lesson_notes', 'lesson_notes_file'
    ]

class OtherDocumentForm(forms.ModelForm):

    class Meta:
        model = Other_Document
        fields = ['lesson', 'document']

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'contatct-form'}))
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("User does not exist.")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active.")
        return super(LoginForm, self).clean(*args, **kwargs)