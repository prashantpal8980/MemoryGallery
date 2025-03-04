from django.shortcuts import render
import os
from django.conf import settings
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def memorygallery(request):
        # image_folder = os.path.join(settings.MEDIA_ROOT, 'gallery')
        # image_urls = [f"/media/gallery/{img}" for img in os.listdir(image_folder) if img.endswith(('jpg', 'jpeg', 'png', 'webp'))]
        # return render(request, 'memoryHome.html', {'image_urls': image_urls})
        image_data = [
        ("/static/images/christian-martinez-neon-city-x.jpg", "Description for image 1"),
        
        
        # Add all 8 images with their descriptions
        ]
        return render(request, "memoryHome.html", {"image_data": image_data})


# def gallery(request):
#     image_folder = os.path.join(settings.MEDIA_ROOT, 'gallery')
#     image_urls = [f"/media/gallery/{img}" for img in os.listdir(image_folder) if img.endswith(('jpg', 'jpeg', 'png', 'webp'))]
#     return render(request, 'gallery.html', {'image_urls': image_urls})

# def gallery(request):
#     image_folder = os.path.join(settings.MEDIA_ROOT, 'gallery')
    
#     # Ensure the folder exists before trying to list files
#     if os.path.exists(image_folder):
#         image_urls = [f"/media/gallery/{img}" for img in os.listdir(image_folder) if img.lower().endswith(('jpg', 'jpeg', 'png', 'webp'))]
#     else:
#         image_urls = []
#     return render(request, 'gallery.html', {'image_urls': image_urls})
@login_required
def gallery(request):
    image_folder = os.path.join(settings.MEDIA_ROOT, 'gallery')
    image_list = [f"/media/gallery/{img}" for img in os.listdir(image_folder) if img.endswith(('jpg', 'jpeg', 'png', 'webp'))]
    
    # Paginate images (12 per page)
    paginator = Paginator(image_list, 10)
    page_number = request.GET.get('page', 1)  # Get page number from URL
    page_obj = paginator.get_page(page_number)  # Get images for that page

    return render(request, 'gallery.html', {'page_obj': page_obj})
