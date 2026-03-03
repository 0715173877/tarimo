from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField  # You'll need to install django-ckeditor

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Display order")
    
    class Meta:
        abstract = True
        ordering = ['order', '-created_at']

class HeroSection(BaseModel):
    """Homepage hero section content"""
    tagline_en = models.CharField(max_length=200, default="Trusted Banking & Mobile Money Agent · Est. 2022")
    tagline_sw = models.CharField(max_length=200, default="Wakala wa Benki na Pesa kwa Simu · Ilianzishwa 2022")
    heading_en = models.CharField(max_length=200, default="Your Trusted Mobile Money & Banking Agent")
    heading_sw = models.CharField(max_length=200, default="Wakala Wako wa Pesa kwa Simu na Benki Anayeaminika")
    subheading_en = models.TextField(max_length=500, default="Fast, secure & reliable financial services in Dodoma. Banking, mobile money & international money transfers under one roof.")
    subheading_sw = models.TextField(max_length=500, default="Huduma za kifedha za haraka, salama na za kuaminika Dodoma. Benki, pesa kwa simu na uhamisho wa fedha kimataifa chini ya paa moja.")
    registration_text_en = models.CharField(max_length=100, default="Reg: 17th May 2022")
    registration_text_sw = models.CharField(max_length=100, default="Sajili: 17 Mei 2022")
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"
        
    def __str__(self):
        return "Hero Section"

class ContactInfo(BaseModel):
    """Contact information"""
    phone = models.CharField(max_length=20, default="+255 788 775 282")
    whatsapp = models.CharField(max_length=20, default="+255 788 775 282")
    email = models.EmailField(default="agtarimo@gmail.com")
    
    working_hours_en = models.CharField(max_length=100, default="Mon-Sat 8:00-20:00 | Sun 8:30-20:00")
    working_hours_sw = models.CharField(max_length=100, default="Jumatatu-Jumamosi 8:00-20:00 | Jumapili 8:30-20:00")
    
    notice_en = models.CharField(max_length=200, default="WhatsApp/SMS/Voice calls accepted during working hours only")
    notice_sw = models.CharField(max_length=200, default="WhatsApp/SMS/Simu hupokelewa wakati wa saa za kazi tu")
    
    class Meta:
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"
        
    def __str__(self):
        return "Contact Info"

class AboutSection(BaseModel):
    """About page sections (Vision, Mission, Values)"""
    SECTION_TYPES = [
        ('vision', 'Vision'),
        ('mission', 'Mission'),
        ('values', 'Core Values'),
    ]
    
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES, unique=True)
    title_en = models.CharField(max_length=100)
    title_sw = models.CharField(max_length=100)
    content_en = models.TextField()
    content_sw = models.TextField()
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class", default="bi-eye")
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Sections"
        
    def __str__(self):
        return f"{self.get_section_type_display()}"

class CoreService(BaseModel):
    """Core services cards"""
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class", default="bi-bank2")
    title_en = models.CharField(max_length=100)
    title_sw = models.CharField(max_length=100)
    description_en = models.CharField(max_length=300)
    description_sw = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = "Core Service"
        verbose_name_plural = "Core Services"
        
    def __str__(self):
        return self.title_en

class Branch(BaseModel):
    """Branches"""
    name_en = models.CharField(max_length=100)
    name_sw = models.CharField(max_length=100)
    address_en = models.TextField()
    address_sw = models.TextField()
    postal_box = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    is_main = models.BooleanField(default=False)
    is_coming_soon = models.BooleanField(default=False)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
        
    def __str__(self):
        return self.name_en

class Location(BaseModel):
    """Location details with map"""
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE, related_name='location_details')
    street_address_en = models.CharField(max_length=200)
    street_address_sw = models.CharField(max_length=200)
    landmark_en = models.TextField(blank=True)
    landmark_sw = models.TextField(blank=True)
    google_maps_embed_url = models.URLField(max_length=500, blank=True)
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        
    def __str__(self):
        return f"Location: {self.branch.name_en}"

class CarouselSlide(BaseModel):
    """Homepage carousel slides"""
    title_en = models.CharField(max_length=200)
    title_sw = models.CharField(max_length=200)
    description_en = models.TextField()
    description_sw = models.TextField()
    badge_text_en = models.CharField(max_length=100)
    badge_text_sw = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel/')
    image_url = models.URLField(blank=True, help_text="External image URL (if no image uploaded)")
    
    class Meta:
        verbose_name = "Carousel Slide"
        verbose_name_plural = "Carousel Slides"
        
    def __str__(self):
        return self.title_en

class PartnerBank(BaseModel):
    """Partner banks"""
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, default="Commercial Bank")
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Partner Bank"
        verbose_name_plural = "Partner Banks"
        
    def __str__(self):
        return self.name

class MobileOperator(BaseModel):
    """Mobile money operators"""
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Mobile Money Operator"
        verbose_name_plural = "Mobile Money Operators"
        
    def __str__(self):
        return self.name

class TransferPartner(BaseModel):
    """International money transfer partners"""
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Transfer Partner"
        verbose_name_plural = "Transfer Partners"
        
    def __str__(self):
        return self.name

class FAQ(BaseModel):
    """Frequently Asked Questions"""
    question_en = models.CharField(max_length=300)
    question_sw = models.CharField(max_length=300)
    answer_en = models.TextField()
    answer_sw = models.TextField()
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['order']
        
    def __str__(self):
        return self.question_en[:50]

class VisitorCounter(BaseModel):
    """Website visitor counter"""
    count = models.IntegerField(default=1234)
    text_en = models.CharField(max_length=50, default="and counting...")
    text_sw = models.CharField(max_length=50, default="na zinaendelea...")
    
    class Meta:
        verbose_name = "Visitor Counter"
        verbose_name_plural = "Visitor Counter"
        
    def __str__(self):
        return f"Visitors: {self.count}"

class FooterContent(BaseModel):
    """Footer content"""
    company_name = models.CharField(max_length=100, default="KALTON INVESTMENT")
    registration_en = models.CharField(max_length=200)
    registration_sw = models.CharField(max_length=200)
    address_en = models.TextField()
    address_sw = models.TextField()
    copyright_text = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = "Footer Content"
        verbose_name_plural = "Footer Content"
        
    def __str__(self):
        return "Footer"

class SocialMediaLink(BaseModel):
    """Social media links"""
    platform = models.CharField(max_length=50, choices=[
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('whatsapp', 'WhatsApp'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
    ])
    url = models.URLField()
    icon = models.CharField(max_length=50, help_text="Bootstrap icon class")
    
    class Meta:
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"
        
    def __str__(self):
        return self.platform

class WebsiteSetting(models.Model):
    """Global website settings"""
    site_name = models.CharField(max_length=100, default="Kalton Investment")
    primary_color = models.CharField(max_length=20, default="#f5b342")
    favicon = models.ImageField(upload_to='settings/', blank=True, null=True)
    logo = models.ImageField(upload_to='settings/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Website Setting"
        verbose_name_plural = "Website Settings"
        
    def __str__(self):
        return self.site_name