from django.shortcuts import render

# Create your views here.
def memorygallery(request):
    return render(request, 'memoryHome.html')