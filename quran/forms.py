from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField 
from django_recaptcha.widgets import ReCaptchaV2Checkbox 
from django.contrib.auth import get_user_model
from tinymce.widgets import TinyMCE

class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")
class SignupForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'image', 'description']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or email '}),
        label="Username ")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    capthca=ReCaptchaField(widget=ReCaptchaV2Checkbox)
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'image', 'description']
        

class SeriesCreateForm(forms.ModelForm):
    class Meta:
        model = ArticleSeries

        fields = [
            "title",
            "subtitle",
            "slug",
            "image",
        ]
class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            "title",
            "subtitle",
            "article_slug",
            "content",
            "notes",
            "series",
            "image",
        ]

class SeriesUpdateForm(forms.ModelForm):
    class Meta:
        model = ArticleSeries

        fields = [
            "title",
            "subtitle",
            "image",
        ]

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            "title",
            "subtitle",
            "content",
            "notes",
            "series",
            "image",
        ]

class OrderForm(forms.Form):
    name=forms.CharField(max_length=100, label="Name", widget=forms.TextInput(attrs={'placeholder': 'Enter your account name'}))
    email=forms.EmailField(max_length=100, label="Email", widget=forms.EmailInput(attrs={'placeholder': 'Enter your account email'}))
    phonenumber=forms.IntegerField( widget=forms.NumberInput(attrs={'placeholder': 'Enter your account phonenumber'}))

class FatwaForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name", widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    question = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter the questuion'}), label="Question")
    category = forms.CharField(max_length=100, required=False, label="Category",widget=forms.TextInput(attrs={'placeholder': 'Enter the category of questuion'}))

class ExchangeDetailForm(forms.ModelForm):
    class Meta:
        model = ExchangeDetail
        fields = ['number_cash_wallet', 'screenshot']
        widgets = {
            'number_cash_wallet': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter wallet number'
            }),
            'screenshot': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/jpeg, image/png'
            }),
        }
