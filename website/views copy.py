from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.core.paginator import Paginator
import json

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

# Admin views
@login_required(login_url='website:admin_login')
def admin_panel(request):
    """Admin dashboard"""
    context = {
        'stats': {
            'banks': PartnerBank.objects.count(),
            'mobile': MobileOperator.objects.count(),
            'transfers': TransferPartner.objects.count(),
            'branches': Branch.objects.count(),
            'faqs': FAQ.objects.count(),
            'slides': CarouselSlide.objects.count(),
        }
    }
    return render(request, 'website/admin_panel.html', context)

def admin_login(request):
    """Custom admin login"""
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('------- ', username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('/admin-panel/')
        else:
            context['success'] = False
            context['error']= 'Invalid credentials'
    
    return render(request, 'website/admin_login.html', context)

@login_required
def admin_logout(request):
    logout(request)
    return redirect('/admin-panel/')

# API Views (for AJAX operations)
@login_required
def api_get_section(request, section, pk=None):
    """Get section data for editing"""
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
    """Save section data"""
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
    """Delete section item"""
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
    """Reorder section items"""
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