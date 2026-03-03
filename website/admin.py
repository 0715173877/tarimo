from django.contrib import admin
from django.utils.html import format_html
from .models import *

class BaseModelAdmin(admin.ModelAdmin):
    list_editable = ['order', 'is_active']
    list_display = ['id', 'order', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at']
    
class HeroSectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('English Content', {
            'fields': ('tagline_en', 'heading_en', 'subheading_en', 'registration_text_en')
        }),
        ('Swahili Content', {
            'fields': ('tagline_sw', 'heading_sw', 'subheading_sw', 'registration_text_sw')
        }),
    )
    
class AboutSectionAdmin(BaseModelAdmin):
    list_display = ['section_type', 'title_en', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    fieldsets = (
        ('Section Info', {
            'fields': ('section_type', 'icon', 'order', 'is_active')
        }),
        ('English', {
            'fields': ('title_en', 'content_en')
        }),
        ('Swahili', {
            'fields': ('title_sw', 'content_sw')
        }),
    )

class CoreServiceAdmin(BaseModelAdmin):
    list_display = ['title_en', 'icon_preview', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    
    def icon_preview(self, obj):
        return format_html('<i class="bi {}" style="font-size: 1.5rem;"></i>', obj.icon)
    icon_preview.short_description = 'Icon'

class BranchAdmin(BaseModelAdmin):
    list_display = ['name_en', 'is_main', 'is_coming_soon', 'order', 'is_active']
    list_editable = ['order', 'is_active', 'is_main', 'is_coming_soon']
    list_filter = ['is_main', 'is_coming_soon']

class CarouselSlideAdmin(BaseModelAdmin):
    list_display = ['title_en', 'image_preview', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Preview'

class PartnerBankAdmin(BaseModelAdmin):
    list_display = ['name', 'category', 'order', 'is_active']
    list_editable = ['order', 'is_active']

class FAQAdmin(BaseModelAdmin):
    list_display = ['question_en', 'order', 'is_active']
    list_editable = ['order', 'is_active']

# Register all models
admin.site.register(HeroSection, HeroSectionAdmin)
admin.site.register(ContactInfo)
admin.site.register(AboutSection, AboutSectionAdmin)
admin.site.register(CoreService, CoreServiceAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Location)
admin.site.register(CarouselSlide, CarouselSlideAdmin)
admin.site.register(PartnerBank, PartnerBankAdmin)
admin.site.register(MobileOperator, BaseModelAdmin)
admin.site.register(TransferPartner, BaseModelAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(VisitorCounter)
admin.site.register(FooterContent)
admin.site.register(SocialMediaLink)
admin.site.register(WebsiteSetting)

# Customize admin site
admin.site.site_header = "Kalton Investment Administration"
admin.site.site_title = "Kalton Investment Admin"
admin.site.index_title = "Welcome to Kalton Investment Admin Panel"