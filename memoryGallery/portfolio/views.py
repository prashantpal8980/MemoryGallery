from django.shortcuts import render

# Create your views here.
def portfolio(request):
    
    image="/static/images/test.jpg"
    return render(request, 'portfolio.html',{"image": image})

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
