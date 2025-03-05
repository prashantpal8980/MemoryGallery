from django.shortcuts import render

# Create your views here.
def portfolio(request):
    
    image="/static/images/test.jpg"
    # image="/static/images/besttest2.jpg"
    return render(request, 'portfolio.html',{"image": image})

def projects(request):
    image="/static/images/project_image.jpg"
    return render(request, 'projects.html',{"image": image})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
