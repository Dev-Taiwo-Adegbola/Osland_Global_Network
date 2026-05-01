from django.contrib import admin
from .models import SiteSettings, HomePage, AboutPage, ExportService, ExportMarket, FAQ

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'contact_email', 'contact_phone', 'updated_at')

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('hero_title', 'updated_at')

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('updated_at',)

@admin.register(ExportService)
class ExportServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ExportMarket)
class ExportMarketAdmin(admin.ModelAdmin):
    list_display = ('country_name',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')
