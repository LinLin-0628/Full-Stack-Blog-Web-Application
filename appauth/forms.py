from django import forms
from django.contrib.auth import get_user_model
from .models import CaptchaModel

User = get_user_model()


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100,
                               min_length=1,
                               error_messages={
                                   "required": 'Please enter a username.',
                                   "max_length": 'Username length must be between 1 and 100.',
                                   "min_length": 'Username length must be between 1 and 100.',
                               })

    email = forms.EmailField(
        error_messages={
            "required": 'Please enter an email address.',
            "invalid": 'Please enter a valid email address.',
        }
    )

    captcha = forms.CharField(max_length=4, min_length=4, error_messages={
        "required": 'Please enter a captcha code.',
        "max_length": 'Please enter a valid captcha code.',
        "min_length": 'Please enter a valid captcha code.',
    })

    password = forms.CharField(max_length=64, min_length=4)


    def clean_email(self):
        email = self.cleaned_data['email']
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise forms.ValidationError("Email already registered.")

        return email

    def clean_captcha(self):
        captcha = self.cleaned_data['captcha']
        email = self.cleaned_data['email']

        captcha_model = CaptchaModel.objects.filter(email=email, captcha=captcha).first()

        # If captcha model not exist (email doesn't match with verification code)
        if not captcha_model:
            raise forms.ValidationError("Captcha does not match with email.")

        captcha_model.delete()

        return captcha


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            "required": 'Please enter an email address.',
            "invalid": 'Please enter a valid email address.',
        }
    )

    password = forms.CharField(max_length=64, min_length=4)

    renderer = forms.IntegerField(required=False)


