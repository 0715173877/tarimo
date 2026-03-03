from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'autofocus': True
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )

# Dynamic model forms for each section
class HeroSectionForm(forms.ModelForm):
    class Meta:
        model = HeroSection
        fields = '__all__'
        widgets = {
            'tagline_en': forms.TextInput(attrs={'class': 'form-control'}),
            'tagline_sw': forms.TextInput(attrs={'class': 'form-control'}),
            'heading_en': forms.TextInput(attrs={'class': 'form-control'}),
            'heading_sw': forms.TextInput(attrs={'class': 'form-control'}),
            'subheading_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'subheading_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class AboutSectionForm(forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = '__all__'
        widgets = {
            'content_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'content_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class CoreServiceForm(forms.ModelForm):
    class Meta:
        model = CoreService
        fields = '__all__'
        widgets = {
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'bi-bank2'}),
        }

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class CarouselSlideForm(forms.ModelForm):
    class Meta:
        model = CarouselSlide
        fields = '__all__'
        widgets = {
            'description_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'description_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PartnerBankForm(forms.ModelForm):
    class Meta:
        model = PartnerBank
        fields = '__all__'

class MobileOperatorForm(forms.ModelForm):
    class Meta:
        model = MobileOperator
        fields = '__all__'

class TransferPartnerForm(forms.ModelForm):
    class Meta:
        model = TransferPartner
        fields = '__all__'

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'answer_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'answer_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class VisitorCounterForm(forms.ModelForm):
    class Meta:
        model = VisitorCounter
        fields = '__all__'

class FooterContentForm(forms.ModelForm):
    class Meta:
        model = FooterContent
        fields = '__all__'
        widgets = {
            'address_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'address_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class SocialMediaLinkForm(forms.ModelForm):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'