# website/forms.py
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

# Base form mixin to handle BaseModel fields consistently
class BaseModelFormMixin:
    """Mixin to add consistent handling of BaseModel fields"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Configure is_active field
        if 'is_active' in self.fields:
            self.fields['is_active'].label = "Active Status"
            self.fields['is_active'].help_text = "Uncheck to hide this item from the website"
            # Force override the widget
            self.fields['is_active'].widget = forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch'
            })
            
            # Set initial value for new instances
            if not self.instance.pk:
                self.fields['is_active'].initial = True
        
        # Configure order field - Force override any existing widget
        if 'order' in self.fields:
            self.fields['order'].label = "Display Order"
            self.fields['order'].help_text = "Lower numbers appear first"
            # Force override the widget
            self.fields['order'].widget = forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '1'
            })

class HeroSectionForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = HeroSection
        fields = '__all__'
        widgets = {
            'tagline_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tagline in English'}),
            'tagline_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter tagline in Swahili'}),
            'heading_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading in English'}),
            'heading_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter heading in Swahili'}),
            'subheading_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter subheading in English'}),
            'subheading_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter subheading in Swahili'}),
            'registration_text_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registration text in English'}),
            'registration_text_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registration text in Swahili'}),
            # Note: order and is_active are intentionally omitted here
            # They will be configured by BaseModelFormMixin.__init__
        }

class ContactInfoForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+255 XXX XXX XXX'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+255 XXX XXX XXX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@example.com'}),
            'working_hours_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Working hours in English'}),
            'working_hours_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Working hours in Swahili'}),
            'notice_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notice in English'}),
            'notice_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notice in Swahili'}),
        }

class AboutSectionForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = '__all__'
        widgets = {
            'section_type': forms.Select(attrs={'class': 'form-select'}),
            'title_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title in English'}),
            'title_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title in Swahili'}),
            'content_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter content in English'}),
            'content_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter content in Swahili'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., bi-eye, bi-bullseye'}),
        }

class CoreServiceForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = CoreService
        fields = '__all__'
        widgets = {
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., bi-bank2, bi-phone'}),
            'title_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title in English'}),
            'title_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title in Swahili'}),
            'description_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description in English'}),
            'description_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description in Swahili'}),
        }

class BranchForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
        widgets = {
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch name in English'}),
            'name_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Branch name in Swahili'}),
            'address_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Address in English'}),
            'address_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Address in Swahili'}),
            'postal_box': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'P.O. Box'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+255 XXX XXX XXX'}),
            'is_main': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_coming_soon': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any', 'placeholder': 'Latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any', 'placeholder': 'Longitude'}),
        }

class LocationForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'branch': forms.Select(attrs={'class': 'form-select'}),
            'street_address_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street address in English'}),
            'street_address_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street address in Swahili'}),
            'landmark_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Landmark in English'}),
            'landmark_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Landmark in Swahili'}),
            'google_maps_embed_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Google Maps embed URL'}),
        }

class CarouselSlideForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = CarouselSlide
        fields = '__all__'
        widgets = {
            'title_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title in English'}),
            'title_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title in Swahili'}),
            'description_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description in English'}),
            'description_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Description in Swahili'}),
            'badge_text_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Badge text in English'}),
            'badge_text_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Badge text in Swahili'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'image_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'External image URL'}),
        }

class PartnerBankForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = PartnerBank
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bank name'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class MobileOperatorForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = MobileOperator
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Operator name'}),
        }

class TransferPartnerForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = TransferPartner
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Partner name'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class FAQForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
        widgets = {
            'question_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Question in English'}),
            'question_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Question in Swahili'}),
            'answer_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Answer in English'}),
            'answer_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Answer in Swahili'}),
        }

class VisitorCounterForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = VisitorCounter
        fields = '__all__'
        widgets = {
            'count': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'text_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Text in English'}),
            'text_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Text in Swahili'}),
        }

class FooterContentForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = FooterContent
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company name'}),
            'registration_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registration info in English'}),
            'registration_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Registration info in Swahili'}),
            'address_en': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Address in English'}),
            'address_sw': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Address in Swahili'}),
            'copyright_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Copyright text'}),
        }

class SocialMediaLinkForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'
        widgets = {
            'platform': forms.Select(attrs={'class': 'form-select'}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://...'}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., bi-facebook'}),
        }

class WebsiteSettingForm(forms.ModelForm):
    """Website settings (doesn't inherit BaseModel)"""
    class Meta:
        model = WebsiteSetting
        fields = '__all__'
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Site name'}),
            'primary_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'favicon': forms.FileInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }


# website/forms.py

class PromoBlockForm(BaseModelFormMixin, forms.ModelForm):
    class Meta:
        model = PromoBlock
        fields = '__all__'
        widgets = {
            'title_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title in English'}),
            'title_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title in Swahili'}),
            'description_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description in English'}),
            'description_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter description in Swahili'}),
            'button_text_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Button text in English'}),
            'button_text_sw': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Button text in Swahili'}),
            'button_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., #contact or /contact/'}),
            'button_icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., bi-whatsapp, bi-envelope'}),
            'background_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'text_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
            'accent_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color'}),
        }




# postgres=# CREATE DATABASE kalton_investment_db;
# CREATE DATABASE
# postgres=# \l;
# invalid command \l;
# Try \? for help.
# postgres=# l\
# invalid command \
# Try \? for help.
# postgres-# CREATE USER kalton_user WITH PASSWORD 'kalton@321';
# ERROR:  syntax error at or near "l"
# LINE 1: l
#         ^
# postgres=# CREATE USER kalton_user WITH PASSWORD 'kalton@321';
# CREATE ROLE
# postgres=# GRANT ALL PRIVILEGES ON DATABASE kalton_investment_db TO kalton_user;
# GRANT
# postgres=# ALTER USER kalton_user CREATEDB;
# ALTER ROLE
# postgres=# \q