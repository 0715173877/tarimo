from .models import WebsiteSetting, ContactInfo, PromoBlock

def website_settings(request):
    """Add website settings to all templates"""
    return {
        'site_settings': WebsiteSetting.objects.first(),
        'contact_info': ContactInfo.objects.first(),
    }

def promo_block(request):
    """Make promo block available in all templates"""
    # print('============= ', PromoBlock.objects.first())
    return {
        'promo_block': PromoBlock.objects.first()
    }


