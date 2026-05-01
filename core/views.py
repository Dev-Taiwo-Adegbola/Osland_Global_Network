from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import HomePage, AboutPage, ExportService, ExportMarket, FAQ, SiteSettings
from products.models import Product

class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_content'] = HomePage.objects.first()
        context['latest_products'] = Product.objects.filter(featured=True)[:6]
        context['services'] = ExportService.objects.all()[:3]
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_content'] = AboutPage.objects.first()
        return context

class ServicesView(ListView):
    model = ExportService
    template_name = 'core/services.html'
    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['markets'] = ExportMarket.objects.all()
        return context

class FAQView(ListView):
    model = FAQ
    template_name = 'core/faq.html'
    context_object_name = 'faqs'

class ContactView(TemplateView):
    template_name = 'core/contact.html'
