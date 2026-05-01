from django.urls import path
from . import views

app_name = 'inquiries'

urlpatterns = [
    path('request-quote/', views.InquiryCreateView.as_view(), name='request_quote'),
]
