from .models import WebsiteSetting, ContactInfo

def website_settings(request):
    """Add website settings to all templates"""
    return {
        'site_settings': WebsiteSetting.objects.first(),
        'contact_info': ContactInfo.objects.first(),
    }