from django.core.management.base import BaseCommand
from website.models import *

class Command(BaseCommand):
    help = 'Load initial data for Kalton Investment website'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading initial data...')
        
        # Create Hero Section
        HeroSection.objects.get_or_create(
            tagline_en="Trusted Banking & Mobile Money Agent · Est. 2022",
            tagline_sw="Wakala wa Benki na Pesa kwa Simu · Ilianzishwa 2022",
            heading_en="Your Trusted Mobile Money & Banking Agent",
            heading_sw="Wakala Wako wa Pesa kwa Simu na Benki Anayeaminika",
            subheading_en="Fast, secure & reliable financial services in Dodoma. Banking, mobile money & international money transfers under one roof.",
            subheading_sw="Huduma za kifedha za haraka, salama na za kuaminika Dodoma. Benki, pesa kwa simu na uhamisho wa fedha kimataifa chini ya paa moja.",
            registration_text_en="Reg: 17th May 2022",
            registration_text_sw="Sajili: 17 Mei 2022"
        )
        
        # Create Contact Info
        ContactInfo.objects.get_or_create(
            phone="+255 788 775 282",
            whatsapp="+255 788 775 282",
            email="agtarimo@gmail.com",
            working_hours_en="Mon-Sat 8:00-20:00 | Sun 8:30-20:00",
            working_hours_sw="Jumatatu-Jumamosi 8:00-20:00 | Jumapili 8:30-20:00",
            notice_en="WhatsApp/SMS/Voice calls accepted during working hours only",
            notice_sw="WhatsApp/SMS/Simu hupokelewa wakati wa saa za kazi tu"
        )
        
        # Create About Sections
        AboutSection.objects.get_or_create(
            section_type='vision',
            defaults={
                'title_en': 'Our Vision',
                'title_sw': 'Maono Yetu',
                'content_en': 'To be the most trusted and accessible financial services provider in Dodoma region, bridging the gap between traditional banking and mobile money.',
                'content_sw': 'Kuwa mtoa huduma wa kifedha anayeaminika na anayepatikana kwa urahisi katika mkoa wa Dodoma, kuunganisha benki za jadi na pesa kwa simu.',
                'icon': 'bi-eye',
                'order': 0
            }
        )
        
        AboutSection.objects.get_or_create(
            section_type='mission',
            defaults={
                'title_en': 'Our Mission',
                'title_sw': 'Dhamira Yetu',
                'content_en': 'To provide fast, reliable, and secure financial services to our community through innovative solutions and exceptional customer service.',
                'content_sw': 'Kutoa huduma za kifedha za haraka, za kuaminika na salama kwa jamii yetu kupitia suluhisho bunifu na huduma bora kwa wateja.',
                'icon': 'bi-bullseye',
                'order': 1
            }
        )
        
        AboutSection.objects.get_or_create(
            section_type='values',
            defaults={
                'title_en': 'Core Values',
                'title_sw': 'Maadili Yetu',
                'content_en': 'Trust, Integrity, Accessibility, Innovation, and Customer-Centric Service in everything we do.',
                'content_sw': 'Uaminifu, Uadilifu, Upatikanaji, Ubunifu, na Huduma inayomlenga Mteja katika kila tunachofanya.',
                'icon': 'bi-gem',
                'order': 2
            }
        )
        
        # Create Core Services
        services = [
            ('Banking Agency', 'Uwakala wa Benki', 'bi-bank2', 
             'CRDB, NMB, NBC, Equity, TCB, Akiba, Mkombozi, Amana, Mwanga Hakika, Mwalimu & more',
             'CRDB, NMB, NBC, Equity, TCB, Akiba, Mkombozi, Amana, Mwanga Hakika, Mwalimu na wengine'),
            ('Mobile Money', 'Pesa kwa Simu', 'bi-phone',
             'Airtel, M-Pesa, Mixx by Yas, Halo Pesa, T-Pesa, Selcom',
             'Airtel, M-Pesa, Mixx by Yas, Halo Pesa, T-Pesa, Selcom'),
            ('International Money Transfers', 'Uhamisho Fedha Kimataifa', 'bi-send',
             'Western Union · MoneyGram Send & receive worldwide',
             'Western Union · MoneyGram Tuma na pokea duniani'),
            ('Working Hours', 'Saa za Kazi', 'bi-clock',
             'Mon-Sat 8:00–20:00 Sun 8:30–20:00',
             'Jumatatu-Jumamosi 8:00–20:00 Jumapili 8:30–20:00'),
        ]
        
        for i, (en_title, sw_title, icon, en_desc, sw_desc) in enumerate(services):
            CoreService.objects.get_or_create(
                title_en=en_title,
                defaults={
                    'title_sw': sw_title,
                    'icon': icon,
                    'description_en': en_desc,
                    'description_sw': sw_desc,
                    'order': i
                }
            )
        
        # Create Branches
        main_branch = Branch.objects.get_or_create(
            name_en='Main Branch',
            defaults={
                'name_sw': 'Tawi Kuu',
                'address_en': 'Morogoro Road/Nzuguni Street, Nzuguni Area, Dodoma',
                'address_sw': 'Morogoro Road/Nzuguni Street, Nzuguni Area, Dodoma',
                'postal_box': 'P.O. Box 4236 Dodoma',
                'phone': '+255 788 775 282',
                'is_main': True,
                'order': 0
            }
        )[0]
        
        Branch.objects.get_or_create(
            name_en='Coming Soon',
            defaults={
                'name_sw': 'Inakuja Karibuni',
                'address_en': 'Additional branches opening in Dodoma',
                'address_sw': 'Matawi zaidi yanafunguliwa Dodoma',
                'is_coming_soon': True,
                'order': 1
            }
        )
        
        # Create Location for main branch
        Location.objects.get_or_create(
            branch=main_branch,
            defaults={
                'street_address_en': 'Morogoro Road / Nzuguni Street, Nzuguni Area, Dodoma, Tanzania',
                'street_address_sw': 'Morogoro Road / Nzuguni Street, Nzuguni Area, Dodoma, Tanzania',
                'landmark_en': 'Located in the heart of Nzuguni Area, easily accessible from Morogoro Road. Look for Victoria Complex Building.',
                'landmark_sw': 'Iko katikati ya Nzuguni, inapatikana kwa urahisi kutoka Morogoro Road. Tafuta Jengo la Victoria Complex.',
                'google_maps_embed_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15839.123456789012!2d35.738726!3d-6.163315!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x184c4e5d5e5b5b5b%3A0x5b5b5b5b5b5b5b5b!2sVictoria%20Complex%2C%20Nzuguni%2C%20Dodoma!5e0!3m2!1sen!2stz!4v1647884567890!5m2!1sen!2stz'
            }
        )
        
        # Create Partner Banks
        banks = ['CRDB', 'NMB', 'NBC', 'Equity', 'TCB', 'Azania', 'PBZ', 'Exim', 'BOA', 'Stanbic', 
                 'Absa', 'UBA', 'Access', 'DTB', 'Mwalimu Commercial Bank', 'Akiba Commercial Bank',
                 'Mkombozi Commercial Bank', 'Amana Bank', 'Mwanga Hakika Bank']
        
        for i, bank in enumerate(banks):
            PartnerBank.objects.get_or_create(
                name=bank,
                defaults={'order': i}
            )
        
        # Create Mobile Operators
        operators = ['Airtel Money', 'M-Pesa', 'Mixx by Yas', 'Halo Pesa', 'T-Pesa', 'Selcom']
        for i, op in enumerate(operators):
            MobileOperator.objects.get_or_create(
                name=op,
                defaults={'order': i}
            )
        
        # Create Transfer Partners
        TransferPartner.objects.get_or_create(name='Western Union', defaults={'order': 0})
        TransferPartner.objects.get_or_create(name='MoneyGram', defaults={'order': 1})
        
        # Create FAQs
        faqs = [
            ('What are your working hours?', 
             'Saa zenu za kazi ni zipi?',
             'We are open Monday to Saturday from 8:00 AM to 8:00 PM, and Sunday from 8:30 AM to 8:00 PM. Our phone lines are available during working hours only.',
             'Tunafunguliwa Jumatatu hadi Jumamosi 8:00 asubuhi hadi 8:00 jioni, na Jumapili 8:30 hadi 8:00 jioni. Simu zetu zinapatikana wakati wa saa za kazi tu.'),
            ('Can I send money internationally through Western Union?',
             'Naweza kutuma pesa kimataifa kupitia Western Union?',
             'Currently, customers can only receive money internationally. We are in the final stages of being allowed to send money internationally. Soon we will offer both sending and receiving services.',
             'Kwa sasa, wateja wanaweza kupokea tu pesa kutoka nje. Tuko katika hatua za mwishzo za kuruhusiwa kutuma pesa kimataifa. Hivi karibuni tutatoa huduma zote za kutuma na kupokea.'),
            ('Where exactly are you located in Dodoma?',
             'Mko wapi hasa Dodoma?',
             'We are located at Victoria Complex Building, along Morogoro Road/Nzuguni Street in Nzuguni Area, Dodoma. Our P.O. Box is 4236 Dodoma.',
             'Tupo Jengo la Victoria Complex, kando ya Morogoro Road/Nzuguni Street katika eneo la Nzuguni, Dodoma. S. L. P ni 4236 Dodoma.'),
            ('How can I submit a complaint?',
             'Ninawezaje kuwasilisha malalamiko?',
             'You can submit complaints via email to agtarimo@gmail.com or call/SMS/WhatsApp +255788775282 during working hours.',
             'Unaweza kuwasilisha malalamiko kwa barua pepe agtarimo@gmail.com au kupiga simu/SMS/WhatsApp +255788775282 wakati wa saa za kazi.'),
        ]
        
        for i, (q_en, q_sw, a_en, a_sw) in enumerate(faqs):
            FAQ.objects.get_or_create(
                question_en=q_en,
                defaults={
                    'question_sw': q_sw,
                    'answer_en': a_en,
                    'answer_sw': a_sw,
                    'order': i
                }
            )
        
        # Create Visitor Counter
        VisitorCounter.objects.get_or_create(
            count=1234,
            text_en='and counting...',
            text_sw='na zinaendelea...'
        )
        
        # Create Footer Content
        FooterContent.objects.get_or_create(
            company_name='KALTON INVESTMENT',
            registration_en='Registered 17th May 2022 · P.O. Box 4236 Dodoma',
            registration_sw='Imejiandikisha 17 Mei 2022 · S. L. P 4236 Dodoma',
            address_en='Victoria Complex Building, Morogoro Road/Nzuguni Street, Nzuguni Area, Dodoma',
            address_sw='Jengo la Victoria Complex, Morogoro Road/Nzuguni Street, Nzuguni Area, Dodoma',
            copyright_text='© 2024 Kalton Investment · All rights reserved'
        )
        
        # Create Social Media Links
        SocialMediaLink.objects.get_or_create(
            platform='facebook',
            defaults={
                'url': 'https://facebook.com',
                'icon': 'bi-facebook',
                'order': 0
            }
        )
        SocialMediaLink.objects.get_or_create(
            platform='instagram',
            defaults={
                'url': 'https://instagram.com',
                'icon': 'bi-instagram',
                'order': 1
            }
        )
        SocialMediaLink.objects.get_or_create(
            platform='whatsapp',
            defaults={
                'url': 'https://wa.me/255788775282',
                'icon': 'bi-whatsapp',
                'order': 2
            }
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))