from django.shortcuts import render
from django.views.generic import ListView
from .models import GalleryImage

class GalleryListView(ListView):
    model = GalleryImage
    template_name = 'gallery/list.html'
    context_object_name = 'images'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GalleryImage.CATEGORY_CHOICES
        context['current_category'] = self.request.GET.get('category')
        return context
