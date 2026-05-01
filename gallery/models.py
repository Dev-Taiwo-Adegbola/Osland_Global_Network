from django.db import models

class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('horns', 'Raw Horns'),
        ('processed', 'Processed'),
        ('hide', 'Hide'),
        ('warehouse', 'Warehouse'),
        ('other', 'Other'),
    ]
    
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else f"Gallery Image {self.id}"
