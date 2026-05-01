from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from products.models import Product, ProductCategory
from inquiries.models import Inquiry
from gallery.models import GalleryImage
from core.models import FAQ, ExportService, ExportMarket, SiteSettings, HomePage, AboutPage

# --- Authentication & Overview ---

class DashboardLoginView(LoginView):
    template_name = 'dashboard/login.html'
    redirect_authenticated_user = True

class DashboardLogoutView(LogoutView):
    next_page = 'dashboard:login'

class DashboardPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'dashboard/settings/password_change.html'
    success_url = reverse_lazy('dashboard:password_change_done')

    def form_valid(self, form):
        messages.success(self.request, "Your password was successfully updated!")
        return super().form_valid(form)

class DashboardPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'dashboard/settings/password_change_done.html'

class DashboardOverviewView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/overview.html'
    login_url = 'dashboard:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_products'] = Product.objects.count()
        context['total_categories'] = ProductCategory.objects.count()
        context['total_inquiries'] = Inquiry.objects.count()
        context['new_inquiries'] = Inquiry.objects.filter(status='new').count()
        context['total_images'] = GalleryImage.objects.count()
        context['recent_inquiries'] = Inquiry.objects.order_by('-created_at')[:5]
        return context

# --- Products Management ---

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'dashboard/products/list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['category', 'name', 'description', 'grade', 'sizes_available', 'packaging_type', 'minimum_order_quantity', 'export_availability', 'image', 'featured']
    template_name = 'dashboard/products/form.html'
    success_url = reverse_lazy('dashboard:product_list')

    def form_valid(self, form):
        messages.success(self.request, "Product created successfully.")
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['category', 'name', 'description', 'grade', 'sizes_available', 'packaging_type', 'minimum_order_quantity', 'export_availability', 'image', 'featured']
    template_name = 'dashboard/products/form.html'
    success_url = reverse_lazy('dashboard:product_list')

    def form_valid(self, form):
        messages.success(self.request, "Product updated successfully.")
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'dashboard/products/confirm_delete.html'
    success_url = reverse_lazy('dashboard:product_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Product deleted successfully.")
        return super().delete(request, *args, **kwargs)

# --- Category Management ---

class CategoryListView(LoginRequiredMixin, ListView):
    model = ProductCategory
    template_name = 'dashboard/categories/list.html'
    context_object_name = 'categories'

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = ProductCategory
    fields = ['name', 'description']
    template_name = 'dashboard/categories/form.html'
    success_url = reverse_lazy('dashboard:category_list')

    def form_valid(self, form):
        messages.success(self.request, "Category created successfully.")
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductCategory
    fields = ['name', 'description']
    template_name = 'dashboard/categories/form.html'
    success_url = reverse_lazy('dashboard:category_list')

    def form_valid(self, form):
        messages.success(self.request, "Category updated successfully.")
        return super().form_valid(form)

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductCategory
    template_name = 'dashboard/categories/confirm_delete.html'
    success_url = reverse_lazy('dashboard:category_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Category deleted successfully.")
        return super().delete(request, *args, **kwargs)

# --- Inquiry Management ---

class InquiryListView(LoginRequiredMixin, ListView):
    model = Inquiry
    template_name = 'dashboard/inquiries/list.html'
    context_object_name = 'inquiries'
    paginate_by = 10
    ordering = ['-created_at']

class InquiryUpdateView(LoginRequiredMixin, UpdateView):
    model = Inquiry
    fields = ['status']
    template_name = 'dashboard/inquiries/detail.html'
    success_url = reverse_lazy('dashboard:inquiry_list')

    def form_valid(self, form):
        messages.success(self.request, f"Inquiry status updated to {self.object.get_status_display()}.")
        return super().form_valid(form)

# --- Gallery Management ---

class GalleryListView(LoginRequiredMixin, ListView):
    model = GalleryImage
    template_name = 'dashboard/gallery/list.html'
    context_object_name = 'images'
    paginate_by = 12
    ordering = ['-uploaded_at']

class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = GalleryImage
    fields = ['image', 'title', 'category']
    template_name = 'dashboard/gallery/form.html'
    success_url = reverse_lazy('dashboard:gallery_list')

    def form_valid(self, form):
        messages.success(self.request, "Gallery image uploaded successfully.")
        return super().form_valid(form)

class GalleryUpdateView(LoginRequiredMixin, UpdateView):
    model = GalleryImage
    fields = ['image', 'title', 'category']
    template_name = 'dashboard/gallery/form.html'
    success_url = reverse_lazy('dashboard:gallery_list')

    def form_valid(self, form):
        messages.success(self.request, "Gallery image updated successfully.")
        return super().form_valid(form)

class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = GalleryImage
    template_name = 'dashboard/gallery/confirm_delete.html'
    success_url = reverse_lazy('dashboard:gallery_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Gallery image deleted successfully.")
        return super().delete(request, *args, **kwargs)

# --- Site Settings & Page Content ---

class SiteSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = SiteSettings
    fields = [
        'site_name', 'logo', 'contact_email', 'contact_phone', 'address',
        'whatsapp_number', 'facebook_url', 'instagram_url', 'linkedin_url',
        'google_maps_embed_url'
    ]
    template_name = 'dashboard/settings/site_settings.html'
    success_url = reverse_lazy('dashboard:site_settings')

    def get_object(self, queryset=None):
        return SiteSettings.objects.first() or SiteSettings.objects.create(site_name="Osland Global Network")

    def form_valid(self, form):
        messages.success(self.request, "Site settings updated successfully.")
        return super().form_valid(form)

class HomePageUpdateView(LoginRequiredMixin, UpdateView):
    model = HomePage
    fields = [
        'hero_title', 'hero_subtitle', 'hero_image',
        'about_section_title', 'about_section_content', 'about_section_image',
        'mission_statement', 'vision_statement'
    ]
    template_name = 'dashboard/settings/home_page.html'
    success_url = reverse_lazy('dashboard:home_page_settings')

    def get_object(self, queryset=None):
        return HomePage.objects.first() or HomePage.objects.create(hero_title="Empowering Global Trade")

    def form_valid(self, form):
        messages.success(self.request, "Home page content updated successfully.")
        return super().form_valid(form)

class AboutPageUpdateView(LoginRequiredMixin, UpdateView):
    model = AboutPage
    fields = [
        'title', 'main_content', 'main_image',
        'experience_years', 'happy_clients'
    ]
    template_name = 'dashboard/settings/about_page.html'
    success_url = reverse_lazy('dashboard:about_page_settings')

    def get_object(self, queryset=None):
        return AboutPage.objects.first() or AboutPage.objects.create(title="About Osland Global Network")

    def form_valid(self, form):
        messages.success(self.request, "About page content updated successfully.")
        return super().form_valid(form)

# --- Content Management (FAQ, Services, Markets) ---

class FAQListView(LoginRequiredMixin, ListView):
    model = FAQ
    template_name = 'dashboard/content/faq_list.html'
    context_object_name = 'faqs'

class FAQCreateView(LoginRequiredMixin, CreateView):
    model = FAQ
    fields = ['question', 'answer']
    template_name = 'dashboard/content/faq_form.html'
    success_url = reverse_lazy('dashboard:faq_list')

    def form_valid(self, form):
        messages.success(self.request, "FAQ added successfully.")
        return super().form_valid(form)

class FAQUpdateView(LoginRequiredMixin, UpdateView):
    model = FAQ
    fields = ['question', 'answer']
    template_name = 'dashboard/content/faq_form.html'
    success_url = reverse_lazy('dashboard:faq_list')

    def form_valid(self, form):
        messages.success(self.request, "FAQ updated successfully.")
        return super().form_valid(form)

class FAQDeleteView(LoginRequiredMixin, DeleteView):
    model = FAQ
    template_name = 'dashboard/content/confirm_delete.html'
    success_url = reverse_lazy('dashboard:faq_list')

class ExportServiceListView(LoginRequiredMixin, ListView):
    model = ExportService
    template_name = 'dashboard/content/service_list.html'
    context_object_name = 'services'

class ExportServiceCreateView(LoginRequiredMixin, CreateView):
    model = ExportService
    fields = ['title', 'description']
    template_name = 'dashboard/content/service_form.html'
    success_url = reverse_lazy('dashboard:service_list')

class ExportServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = ExportService
    fields = ['title', 'description']
    template_name = 'dashboard/content/service_form.html'
    success_url = reverse_lazy('dashboard:service_list')

class ExportServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = ExportService
    template_name = 'dashboard/content/confirm_delete.html'
    success_url = reverse_lazy('dashboard:service_list')

class ExportMarketListView(LoginRequiredMixin, ListView):
    model = ExportMarket
    template_name = 'dashboard/content/market_list.html'
    context_object_name = 'markets'

class ExportMarketCreateView(LoginRequiredMixin, CreateView):
    model = ExportMarket
    fields = ['country_name']
    template_name = 'dashboard/content/market_form.html'
    success_url = reverse_lazy('dashboard:market_list')

class ExportMarketDeleteView(LoginRequiredMixin, DeleteView):
    model = ExportMarket
    template_name = 'dashboard/content/confirm_delete.html'
    success_url = reverse_lazy('dashboard:market_list')
