from django.shortcuts import render
import os
from django.conf import settings
# Create your views here.
def memorygallery(request):
        image_folder = os.path.join(settings.MEDIA_ROOT, 'gallery')
        image_urls = [f"/media/gallery/{img}" for img in os.listdir(image_folder) if img.endswith(('jpg', 'jpeg', 'png', 'webp'))]
        return render(request, 'memoryHome.html', {'image_urls': image_urls})