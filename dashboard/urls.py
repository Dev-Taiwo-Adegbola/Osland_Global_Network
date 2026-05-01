from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', views.DashboardLoginView.as_view(), name='login'),
    path('logout/', views.DashboardLogoutView.as_view(), name='logout'),
    path('password-change/', views.DashboardPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.DashboardPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.DashboardOverviewView.as_view(), name='overview'),

    # Products
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/add/', views.ProductCreateView.as_view(), name='product_add'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # Categories
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    # Inquiries
    path('inquiries/', views.InquiryListView.as_view(), name='inquiry_list'),
    path('inquiries/<int:pk>/', views.InquiryUpdateView.as_view(), name='inquiry_detail'),

    # Gallery
    path('gallery/', views.GalleryListView.as_view(), name='gallery_list'),
    path('gallery/add/', views.GalleryCreateView.as_view(), name='gallery_add'),
    path('gallery/<int:pk>/edit/', views.GalleryUpdateView.as_view(), name='gallery_edit'),
    path('gallery/<int:pk>/delete/', views.GalleryDeleteView.as_view(), name='gallery_delete'),

    # Content (FAQ, Services, Markets)
    path('faqs/', views.FAQListView.as_view(), name='faq_list'),
    path('faqs/add/', views.FAQCreateView.as_view(), name='faq_add'),
    path('faqs/<int:pk>/edit/', views.FAQUpdateView.as_view(), name='faq_edit'),
    path('faqs/<int:pk>/delete/', views.FAQDeleteView.as_view(), name='faq_delete'),

    path('services/', views.ExportServiceListView.as_view(), name='service_list'),
    path('services/add/', views.ExportServiceCreateView.as_view(), name='service_add'),
    path('services/<int:pk>/edit/', views.ExportServiceUpdateView.as_view(), name='service_edit'),
    path('services/<int:pk>/delete/', views.ExportServiceDeleteView.as_view(), name='service_delete'),

    path('markets/', views.ExportMarketListView.as_view(), name='market_list'),
    path('markets/add/', views.ExportMarketCreateView.as_view(), name='market_add'),
    path('markets/<int:pk>/delete/', views.ExportMarketDeleteView.as_view(), name='market_delete'),

    # Settings & Page Content
    path('settings/site/', views.SiteSettingsUpdateView.as_view(), name='site_settings'),
    path('settings/home/', views.HomePageUpdateView.as_view(), name='home_page_settings'),
    path('settings/about/', views.AboutPageUpdateView.as_view(), name='about_page_settings'),
]
