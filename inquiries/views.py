from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Inquiry
from .forms import InquiryForm
from products.models import Product

class InquiryCreateView(SuccessMessageMixin, CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'inquiries/request_quote.html'
    success_url = reverse_lazy('inquiries:request_quote')
    success_message = "Your inquiry has been sent successfully. Our team will contact you shortly."

    def get_initial(self):
        initial = super().get_initial()
        product_id = self.request.GET.get('product')
        if product_id:
            try:
                product = Product.objects.get(id=product_id)
                initial['product_needed'] = product.name
            except Product.DoesNotExist:
                pass
        return initial
