from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    
    # Admin Authentication
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),  # Keep this as is
    
    # Hero Section
    path('admin/hero/', views.admin_hero, name='admin_hero'),
    
    # Contact
    path('admin/contact/', views.admin_contact, name='admin_contact'),
    
    # About Sections
    path('admin/about/', views.admin_about_list, name='admin_about_list'),
    path('admin/about/add/', views.admin_about_edit, name='admin_about_add'),
    path('admin/about/<int:pk>/edit/', views.admin_about_edit, name='admin_about_edit'),
    path('admin/about/<int:pk>/delete/', views.admin_about_delete, name='admin_about_delete'),
    
    # Core Services
    path('admin/core-services/', views.admin_core_services, name='admin_core_services'),
    path('admin/core-services/add/', views.admin_core_service_edit, name='admin_core_service_add'),
    path('admin/core-services/<int:pk>/edit/', views.admin_core_service_edit, name='admin_core_service_edit'),
    path('admin/core-services/<int:pk>/delete/', views.admin_core_service_delete, name='admin_core_service_delete'),
    path('admin/core-services/reorder/', views.admin_core_service_reorder, name='admin_core_service_reorder'),
    
    # Branches
    path('admin/branches/', views.admin_branches, name='admin_branches'),
    path('admin/branches/add/', views.admin_branch_edit, name='admin_branch_add'),
    path('admin/branches/<int:pk>/edit/', views.admin_branch_edit, name='admin_branch_edit'),
    path('admin/branches/<int:pk>/delete/', views.admin_branch_delete, name='admin_branch_delete'),
    
    # Location
    path('admin/location/', views.admin_location, name='admin_location'),
    
    # FAQs
    path('admin/faqs/', views.admin_faqs, name='admin_faqs'),
    path('admin/faqs/add/', views.admin_faq_edit, name='admin_faq_add'),
    path('admin/faqs/<int:pk>/edit/', views.admin_faq_edit, name='admin_faq_edit'),
    path('admin/faqs/<int:pk>/delete/', views.admin_faq_delete, name='admin_faq_delete'),
    
    # Carousel
    path('admin/carousel/', views.admin_carousel, name='admin_carousel'),
    path('admin/carousel/add/', views.admin_carousel_edit, name='admin_carousel_add'),
    path('admin/carousel/<int:pk>/edit/', views.admin_carousel_edit, name='admin_carousel_edit'),
    path('admin/carousel/<int:pk>/delete/', views.admin_carousel_delete, name='admin_carousel_delete'),
    
    # Partner Banks
    path('admin/partner-banks/', views.admin_partner_banks, name='admin_partner_banks'),
    path('admin/partner-banks/add/', views.admin_partner_bank_add, name='admin_partner_bank_add'),
    path('admin/partner-banks/<int:pk>/delete/', views.admin_partner_bank_delete, name='admin_partner_bank_delete'),
    
    # Mobile Operators
    path('admin/mobile-operators/', views.admin_mobile_operators, name='admin_mobile_operators'),
    path('admin/mobile-operators/add/', views.admin_mobile_operator_add, name='admin_mobile_operator_add'),
    path('admin/mobile-operators/<int:pk>/delete/', views.admin_mobile_operator_delete, name='admin_mobile_operator_delete'),
    
    # Transfer Partners
    path('admin/transfer-partners/', views.admin_transfer_partners, name='admin_transfer_partners'),
    path('admin/transfer-partners/add/', views.admin_transfer_partner_add, name='admin_transfer_partner_add'),
    path('admin/transfer-partners/<int:pk>/delete/', views.admin_transfer_partner_delete, name='admin_transfer_partner_delete'),
    
    # Visitor Counter
    path('admin/visitor-counter/', views.admin_visitor_counter, name='admin_visitor_counter'),
    
    # Footer
    path('admin/footer/', views.admin_footer, name='admin_footer'),
    
    # Social Media Links
    path('admin/social-links/', views.admin_social_links, name='admin_social_links'),
    path('admin/social-links/add/', views.admin_social_link_edit, name='admin_social_link_add'),
    path('admin/social-links/<int:pk>/edit/', views.admin_social_link_edit, name='admin_social_link_edit'),
    path('admin/social-links/<int:pk>/delete/', views.admin_social_link_delete, name='admin_social_link_delete'),
    
    # Settings
    path('admin/settings/', views.admin_settings, name='admin_settings'),
    
    # API endpoints (keep these if needed)
    path('api/<str:section>/', views.api_get_section, name='api_get_section'),
    path('api/<str:section>/<int:pk>/', views.api_get_section, name='api_get_single'),
    path('api/save/<str:section>/', views.api_save_section, name='api_save_section'),
    path('api/delete/<str:section>/<int:pk>/', views.api_delete_section, name='api_delete_section'),
    path('api/reorder/<str:section>/', views.api_reorder_section, name='api_reorder_section'),
]