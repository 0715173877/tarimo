from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.core.paginator import Paginator
from django.urls import reverse
import json
from datetime import datetime

from .models import *
from .forms import *

# Public views
def home(request):
    """Homepage view with all content"""
    context = {
        'hero': HeroSection.objects.first(),
        'contact': ContactInfo.objects.first(),
        'about_sections': AboutSection.objects.filter(is_active=True).order_by('order'),
        'core_services': CoreService.objects.filter(is_active=True).order_by('order'),
        'carousel_slides': CarouselSlide.objects.filter(is_active=True).order_by('order'),
        'branches': Branch.objects.filter(is_active=True).order_by('-is_main', 'order'),
        'promo': PromoBlock.objects.first(),
        'partner_banks': PartnerBank.objects.filter(is_active=True).order_by('order'),
        'mobile_operators': MobileOperator.objects.filter(is_active=True).order_by('order'),
        'transfer_partners': TransferPartner.objects.filter(is_active=True).order_by('order'),
        'faqs': FAQ.objects.filter(is_active=True).order_by('order'),
        'visitor_counter': VisitorCounter.objects.first(),
        'footer': FooterContent.objects.first(),
        'social_links': SocialMediaLink.objects.filter(is_active=True).order_by('order'),
        'settings': WebsiteSetting.objects.first(),
    }
    
    # Increment visitor counter
    counter = VisitorCounter.objects.first()
    if counter:
        counter.count += 1
        counter.save()
    
    return render(request, 'website/index.html', context)

# Admin Authentication
def admin_login(request):
    """Custom admin login view"""
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('website:admin_panel')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('website:admin_panel')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'website/admin_login.html')

@login_required
def admin_logout(request):
    """Admin logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('website:admin_login')

# Original admin_panel view (keep this)
@login_required
def admin_panel(request):
    """Admin dashboard - original view"""
    context = {
        'stats': {
            'banks': PartnerBank.objects.count(),
            'mobile': MobileOperator.objects.count(),
            'transfers': TransferPartner.objects.count(),
            'branches': Branch.objects.count(),
            'faqs': FAQ.objects.count(),
            'slides': CarouselSlide.objects.count(),
            'core_services': CoreService.objects.count(),
            'visitors': VisitorCounter.objects.first().count if VisitorCounter.objects.first() else 1234,
        },
        'hero': HeroSection.objects.first(),
        'contact': ContactInfo.objects.first(),
        'about_sections': AboutSection.objects.all().order_by('order'),
        'core_services_list': CoreService.objects.all().order_by('order'),
        'branches_list': Branch.objects.all().order_by('-is_main', 'order'),
        'location': Location.objects.first(),
        'main_branch': Branch.objects.filter(is_main=True).first(),
        'faqs_list': FAQ.objects.all().order_by('order'),
        'carousel_slides': CarouselSlide.objects.all().order_by('order'),
        'partner_banks': PartnerBank.objects.all().order_by('order'),
        'mobile_operators': MobileOperator.objects.all().order_by('order'),
        'transfer_partners': TransferPartner.objects.all().order_by('order'),
        'visitor_counter': VisitorCounter.objects.first(),
        'footer': FooterContent.objects.first(),
        'social_links': SocialMediaLink.objects.all().order_by('order'),
        'settings': WebsiteSetting.objects.first(),
        'current_year': datetime.now().year,
    }
    return render(request, 'website/admin/admin_panel.html', context)

# Hero Section Management
@login_required
def admin_hero(request):
    """Manage hero section"""
    hero = HeroSection.objects.first()
    if not hero:
        hero = HeroSection.objects.create()
    
    if request.method == 'POST':
        form = HeroSectionForm(request.POST, instance=hero)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hero section updated successfully!')
            return redirect('website:admin_hero')
    else:
        form = HeroSectionForm(instance=hero)
    
    return render(request, 'website/admin/hero/hero.html', {'form': form})

# Contact Information Management
@login_required
def admin_contact(request):
    """Manage contact information"""
    contact = ContactInfo.objects.first()
    if not contact:
        contact = ContactInfo.objects.create()
    
    if request.method == 'POST':
        form = ContactInfoForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact information updated successfully!')
            return redirect('website:admin_contact')
    else:
        form = ContactInfoForm(instance=contact)
    
    return render(request, 'website/admin/contact/contact.html', {'form': form})

# About Sections Management
@login_required
def admin_about_list(request):
    """List all about sections"""
    sections = AboutSection.objects.all().order_by('order')
    return render(request, 'website/admin/about/about_list.html', {'sections': sections})

@login_required
def admin_about_edit(request, pk=None):
    """Edit or create about section"""
    if pk:
        section = get_object_or_404(AboutSection, pk=pk)
    else:
        section = None
    
    if request.method == 'POST':
        form = AboutSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            messages.success(request, 'About section saved successfully!')
            return redirect('website:admin_about_list')
    else:
        form = AboutSectionForm(instance=section)
    
    return render(request, 'website/admin/about/about_form.html', {'form': form, 'section': section})

@login_required
def admin_about_delete(request, pk):
    """Delete about section"""
    section = get_object_or_404(AboutSection, pk=pk)
    section.delete()
    messages.success(request, 'About section deleted successfully!')
    return redirect('website:admin_about_list')

# Core Services Management
@login_required
def admin_core_services(request):
    """List all core services"""
    services = CoreService.objects.all().order_by('order')
    return render(request, 'website/admin/core/core_services.html', {'services': services})

@login_required
def admin_core_service_edit(request, pk=None):
    """Edit or create core service"""
    if pk:
        service = get_object_or_404(CoreService, pk=pk)
    else:
        service = None
    
    if request.method == 'POST':
        form = CoreServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Core service saved successfully!')
            return redirect('website:admin_core_services')
    else:
        form = CoreServiceForm(instance=service)
    
    return render(request, 'website/admin/core/core_service_form.html', {'form': form, 'service': service})

@login_required
def admin_core_service_delete(request, pk):
    """Delete core service"""
    service = get_object_or_404(CoreService, pk=pk)
    service.delete()
    messages.success(request, 'Core service deleted successfully!')
    return redirect('website:admin_core_services')

@login_required
def admin_core_service_reorder(request):
    """Reorder core services"""
    if request.method == 'POST':
        order_data = request.POST.get('order', '[]')
        try:
            order_list = json.loads(order_data)
            for index, item_id in enumerate(order_list):
                CoreService.objects.filter(pk=item_id).update(order=index)
            messages.success(request, 'Services reordered successfully!')
        except:
            messages.error(request, 'Error reordering services.')
    return redirect('website:admin_core_services')

# Branches Management
@login_required
def admin_branches(request):
    """List all branches"""
    branches = Branch.objects.all().order_by('-is_main', 'order')
    return render(request, 'website/admin/branch/branches.html', {'branches': branches})

@login_required
def admin_branch_edit(request, pk=None):
    """Edit or create branch"""
    if pk:
        branch = get_object_or_404(Branch, pk=pk)
    else:
        branch = None
    
    if request.method == 'POST':
        form = BranchForm(request.POST, instance=branch)
        if form.is_valid():
            # If this is set as main, unset other main branches
            if form.cleaned_data.get('is_main'):
                Branch.objects.filter(is_main=True).update(is_main=False)
            form.save()
            messages.success(request, 'Branch saved successfully!')
            return redirect('website:admin_branches')
    else:
        form = BranchForm(instance=branch)
    
    return render(request, 'website/admin/branch/branch_form.html', {'form': form, 'branch': branch})

@login_required
def admin_branch_delete(request, pk):
    """Delete branch"""
    branch = get_object_or_404(Branch, pk=pk)
    branch.delete()
    messages.success(request, 'Branch deleted successfully!')
    return redirect('website:admin_branches')

# Location Management
@login_required
def admin_location(request):
    """Manage location"""
    location = Location.objects.first()
    if not location:
        # Create location for main branch if exists
        main_branch = Branch.objects.filter(is_main=True).first()
        if main_branch:
            location = Location.objects.create(branch=main_branch)
        else:
            messages.error(request, 'Please create a main branch first.')
            return redirect('website:admin_branches')
    
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            messages.success(request, 'Location updated successfully!')
            return redirect('website:admin_location')
    else:
        form = LocationForm(instance=location)
    
    return render(request, 'website/admin/location/location.html', {'form': form, 'location': location})

# FAQ Management
@login_required
def admin_faqs(request):
    """List all FAQs"""
    faqs = FAQ.objects.all().order_by('order')
    return render(request, 'website/admin/faq/faqs.html', {'faqs': faqs})

@login_required
def admin_faq_edit(request, pk=None):
    """Edit or create FAQ"""
    if pk:
        faq = get_object_or_404(FAQ, pk=pk)
    else:
        faq = None
    
    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ saved successfully!')
            return redirect('website:admin_faqs')
    else:
        form = FAQForm(instance=faq)
    
    return render(request, 'website/admin/faq/faq_form.html', {'form': form, 'faq': faq})

@login_required
def admin_faq_delete(request, pk):
    """Delete FAQ"""
    faq = get_object_or_404(FAQ, pk=pk)
    faq.delete()
    messages.success(request, 'FAQ deleted successfully!')
    return redirect('website:admin_faqs')

# Carousel Slides Management
@login_required
def admin_carousel(request):
    """List all carousel slides"""
    slides = CarouselSlide.objects.all().order_by('order')
    return render(request, 'website/admin/carousel/carousel.html', {'slides': slides})

@login_required
def admin_carousel_edit(request, pk=None):
    """Edit or create carousel slide"""
    if pk:
        slide = get_object_or_404(CarouselSlide, pk=pk)
    else:
        slide = None
    
    if request.method == 'POST':
        form = CarouselSlideForm(request.POST, request.FILES, instance=slide)
        if form.is_valid():
            form.save()
            messages.success(request, 'Carousel slide saved successfully!')
            return redirect('website:admin_carousel')
    else:
        form = CarouselSlideForm(instance=slide)
    
    return render(request, 'website/admin/carousel/carousel_form.html', {'form': form, 'slide': slide})

@login_required
def admin_carousel_delete(request, pk):
    """Delete carousel slide"""
    slide = get_object_or_404(CarouselSlide, pk=pk)
    if slide.image:
        slide.image.delete()  # Delete the image file
    slide.delete()
    messages.success(request, 'Carousel slide deleted successfully!')
    return redirect('website:admin_carousel')

# Partner Banks Management
@login_required
def admin_partner_banks(request):
    """List all partner banks"""
    banks = PartnerBank.objects.all().order_by('order')
    return render(request, 'website/admin/partner/partner_banks.html', {'banks': banks})

@login_required
def admin_partner_bank_add(request):
    """Add new partner bank"""
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            PartnerBank.objects.create(name=name)
            messages.success(request, f'Bank "{name}" added successfully!')
        else:
            messages.error(request, 'Bank name is required.')
    return redirect('website:admin_partner_banks')

@login_required
def admin_partner_bank_delete(request, pk):
    """Delete partner bank"""
    bank = get_object_or_404(PartnerBank, pk=pk)
    name = bank.name
    bank.delete()
    messages.success(request, f'Bank "{name}" deleted successfully!')
    return redirect('website:admin_partner_banks')

# Mobile Operators Management
@login_required
def admin_mobile_operators(request):
    """List all mobile operators"""
    operators = MobileOperator.objects.all().order_by('order')
    return render(request, 'website/admin/mobile_operator/mobile_operators.html', {'operators': operators})

@login_required
def admin_mobile_operator_add(request):
    """Add new mobile operator"""
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            MobileOperator.objects.create(name=name)
            messages.success(request, f'Operator "{name}" added successfully!')
        else:
            messages.error(request, 'Operator name is required.')
    return redirect('website:admin_mobile_operators')

@login_required
def admin_mobile_operator_delete(request, pk):
    """Delete mobile operator"""
    operator = get_object_or_404(MobileOperator, pk=pk)
    name = operator.name
    operator.delete()
    messages.success(request, f'Operator "{name}" deleted successfully!')
    return redirect('website:admin_mobile_operators')

# Transfer Partners Management
@login_required
def admin_transfer_partners(request):
    """List all transfer partners"""
    partners = TransferPartner.objects.all().order_by('order')
    return render(request, 'website/admin/transfer_partners.html', {'partners': partners})

@login_required
def admin_transfer_partner_add(request):
    """Add new transfer partner"""
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            TransferPartner.objects.create(name=name)
            messages.success(request, f'Partner "{name}" added successfully!')
        else:
            messages.error(request, 'Partner name is required.')
    return redirect('website:admin_transfer_partners')

@login_required
def admin_transfer_partner_delete(request, pk):
    """Delete transfer partner"""
    partner = get_object_or_404(TransferPartner, pk=pk)
    name = partner.name
    partner.delete()
    messages.success(request, f'Partner "{name}" deleted successfully!')
    return redirect('website:admin_transfer_partners')

# Visitor Counter Management
@login_required
def admin_visitor_counter(request):
    """Manage visitor counter"""
    counter = VisitorCounter.objects.first()
    if not counter:
        counter = VisitorCounter.objects.create()
    
    if request.method == 'POST':
        form = VisitorCounterForm(request.POST, instance=counter)
        if form.is_valid():
            form.save()
            messages.success(request, 'Visitor counter updated successfully!')
            return redirect('website:admin_visitor_counter')
    else:
        form = VisitorCounterForm(instance=counter)
    
    return render(request, 'website/admin/settings/visitor_counter.html', {'form': form})

# Footer Management
@login_required
def admin_footer(request):
    """Manage footer content"""
    footer = FooterContent.objects.first()
    if not footer:
        footer = FooterContent.objects.create()
    
    if request.method == 'POST':
        form = FooterContentForm(request.POST, instance=footer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Footer updated successfully!')
            return redirect('website:admin_footer')
    else:
        form = FooterContentForm(instance=footer)
    
    return render(request, 'website/admin/footer/footer.html', {'form': form})

# Social Media Links Management
@login_required
def admin_social_links(request):
    """List all social media links"""
    links = SocialMediaLink.objects.all().order_by('order')
    return render(request, 'website/admin/social/social_links.html', {'links': links})

@login_required
def admin_social_link_edit(request, pk=None):
    """Edit or create social media link"""
    if pk:
        link = get_object_or_404(SocialMediaLink, pk=pk)
    else:
        link = None
    
    if request.method == 'POST':
        form = SocialMediaLinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            messages.success(request, 'Social media link saved successfully!')
            return redirect('website:admin_social_links')
    else:
        form = SocialMediaLinkForm(instance=link)
    
    return render(request, 'website/admin/social/social_link_form.html', {'form': form, 'link': link})

@login_required
def admin_social_link_delete(request, pk):
    """Delete social media link"""
    link = get_object_or_404(SocialMediaLink, pk=pk)
    link.delete()
    messages.success(request, 'Social media link deleted successfully!')
    return redirect('website:admin_social_links')

# Settings Management
@login_required
def admin_settings(request):
    """Manage website settings"""
    settings = WebsiteSetting.objects.first()
    if not settings:
        settings = WebsiteSetting.objects.create()
    
    if request.method == 'POST':
        # Handle settings update
        site_name = request.POST.get('site_name')
        primary_color = request.POST.get('primary_color')
        logo = request.FILES.get('logo')
        favicon = request.FILES.get('favicon')
        
        if site_name:
            settings.site_name = site_name
        if primary_color:
            settings.primary_color = primary_color
        if logo:
            settings.logo = logo
        if favicon:
            settings.favicon = favicon
        
        settings.save()
        messages.success(request, 'Settings updated successfully!')
        return redirect('website:admin_settings')
    
    return render(request, 'website/admin/settings/settings.html', {'settings': settings})


# website/views.py

# Promo Block Management
@login_required
def admin_promo_block(request):
    """Manage promo block"""
    promo = PromoBlock.objects.first()
    if not promo:
        promo = PromoBlock.objects.create()
    
    if request.method == 'POST':
        form = PromoBlockForm(request.POST, instance=promo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promotional block updated successfully!')
            return redirect('website:admin_promo_block')
    else:
        form = PromoBlockForm(instance=promo)
    
    return render(request, 'website/admin/promo/promo_block.html', {'form': form, 'promo': promo})

# Public view to get promo block data (for AJAX if needed)
@login_required
@csrf_exempt
def get_promo_block(request):
    """Return promo block data as JSON"""
    promo = PromoBlock.objects.first()
    if not promo:
        promo = PromoBlock.objects.create()
    
    data = {
        'id': promo.id,
        'title_en': promo.title_en,
        'title_sw': promo.title_sw,
        'description_en': promo.description_en,
        'description_sw': promo.description_sw,
        'button_text_en': promo.button_text_en,
        'button_text_sw': promo.button_text_sw,
        'button_link': promo.button_link,
        'button_icon': promo.button_icon,
        'background_color': promo.background_color,
        'text_color': promo.text_color,
        'accent_color': promo.accent_color,
        'is_active': promo.is_active,
    }
    return JsonResponse(data)

# Keep your existing API views
@login_required
def api_get_section(request, section, pk=None):
    """Get section data for editing (API)"""
    models_map = {
        'core-service': CoreService,
        'branch': Branch,
        'faq': FAQ,
        'about': AboutSection,
        'carousel': CarouselSlide,
        'partner': PartnerBank,
        'mobile': MobileOperator,
        'transfer': TransferPartner,
    }
    
    model_class = models_map.get(section)
    if not model_class:
        return JsonResponse({'error': 'Invalid section'}, status=400)
    
    if pk:
        obj = get_object_or_404(model_class, pk=pk)
        data = {field.name: getattr(obj, field.name) for field in model_class._meta.fields}
        return JsonResponse(data)
    else:
        queryset = model_class.objects.filter(is_active=True).order_by('order')
        data = list(queryset.values())
        return JsonResponse(data, safe=False)

@login_required
@csrf_exempt
def api_save_section(request, section):
    """Save section data (API)"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    models_map = {
        'core-service': CoreService,
        'branch': Branch,
        'faq': FAQ,
        'about': AboutSection,
        'carousel': CarouselSlide,
        'partner': PartnerBank,
        'mobile': MobileOperator,
        'transfer': TransferPartner,
        'hero': HeroSection,
        'contact': ContactInfo,
        'location': Location,
        'footer': FooterContent,
    }
    
    model_class = models_map.get(section)
    if not model_class:
        return JsonResponse({'error': 'Invalid section'}, status=400)
    
    try:
        data = json.loads(request.body)
        
        if data.get('id'):
            obj = model_class.objects.get(pk=data['id'])
            for key, value in data.items():
                setattr(obj, key, value)
            obj.save()
        else:
            obj = model_class.objects.create(**data)
        
        return JsonResponse({'success': True, 'id': obj.id})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@login_required
@csrf_exempt
def api_delete_section(request, section, pk):
    """Delete section item (API)"""
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    models_map = {
        'core-service': CoreService,
        'branch': Branch,
        'faq': FAQ,
        'about': AboutSection,
        'carousel': CarouselSlide,
        'partner': PartnerBank,
        'mobile': MobileOperator,
        'transfer': TransferPartner,
    }
    
    model_class = models_map.get(section)
    if not model_class:
        return JsonResponse({'error': 'Invalid section'}, status=400)
    
    try:
        obj = model_class.objects.get(pk=pk)
        obj.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@login_required
@csrf_exempt
def api_reorder_section(request, section):
    """Reorder section items (API)"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    models_map = {
        'core-service': CoreService,
        'branch': Branch,
        'faq': FAQ,
        'about': AboutSection,
        'carousel': CarouselSlide,
        'partner': PartnerBank,
        'mobile': MobileOperator,
        'transfer': TransferPartner,
    }
    
    model_class = models_map.get(section)
    if not model_class:
        return JsonResponse({'error': 'Invalid section'}, status=400)
    
    try:
        data = json.loads(request.body)
        order_list = data.get('order', [])
        
        for index, item_id in enumerate(order_list):
            model_class.objects.filter(pk=item_id).update(order=index)
        
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)
    


