from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            'full_name', 'company_name', 'country', 'email', 
            'phone', 'product_needed', 'quantity', 'message'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'w-full px-6 py-4 bg-gray-50 border-none rounded-2xl focus:ring-2 focus:ring-blue-600 transition', 'placeholder': 'Full Name *'}),
            'company_name': forms.TextInput(attrs={'class': 'w-full px-6 py-4 bg-gray-50 border-none rounded-2xl focus:ring-2 focus:ring-blue-600 transition', 'placeholder': 'Company Name (Optional)'}),
            'country': forms.TextInput(attrs={'class': 'w-full px-6 py-4 bg-gray-50 border-none rounded-2xl focus:ring-2 focus:ring-blue-600 transition', 'placeholder': 'Country *'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-6 py-4 bg-gray-50 border-none rounded-2xl focus:ring-2 focus:ring-blue-600 transition', 'placeholder': 'Email Address *'}),
            'phone': forms.TextInput(attrs={'class': 'w-full px-6 py-4 bg-gray-50 border-none rounded-2xl focus:ring-2 focus:ring-blue-600 transition', 'placeholder': 'Phone Number *'}),
            'product_needed': forms.TextInput(attrs={'class': 'w-full px-6 py-4 bg-gray-50 border-none rounded-2xl focus:ring-2 focus:ring-blue-600 transition', 'placeholder': 'Product Needed *'}),
            'quantity': forms.TextInput(attrs={'class': 'w-full px-6 py-4 bg-gray-50 border-none rounded-2xl focus:ring-2 focus:ring-blue-600 transition', 'placeholder': 'Approximate Quantity *'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-6 py-4 bg-gray-50 border-none rounded-2xl focus:ring-2 focus:ring-blue-600 transition', 'placeholder': 'Detailed Message *', 'rows': 5}),
        }
