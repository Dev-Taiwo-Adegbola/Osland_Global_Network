from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, default="Osland Global Network")
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    whatsapp_number = models.CharField(max_length=50, blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    google_maps_embed_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name

class HomePage(models.Model):
    hero_title = models.CharField(max_length=255)
    hero_subtitle = models.TextField()
    hero_image = models.ImageField(upload_to='home/', blank=True, null=True)
    about_section_title = models.CharField(max_length=255, blank=True, null=True)
    about_section_content = models.TextField(blank=True, null=True)
    about_section_image = models.ImageField(upload_to='home/', blank=True, null=True)
    mission_statement = models.TextField(blank=True, null=True)
    vision_statement = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Home Page Content"

    def __str__(self):
        return "Home Page Content"

class AboutPage(models.Model):
    title = models.CharField(max_length=255, default="About Us")
    main_content = models.TextField(blank=True, null=True)
    main_image = models.ImageField(upload_to='about/', blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)
    happy_clients = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Page Content"

    def __str__(self):
        return self.title

class ExportService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class ExportMarket(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
