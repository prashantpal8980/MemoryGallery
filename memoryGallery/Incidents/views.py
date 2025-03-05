from django.shortcuts import render
from .forms import IncidentForm, UserRegistrationForm
from .models import Incident
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

@login_required
def IncidentSeenHere(request):
    incidents=Incident.objects.all().order_by('-created_at')
    return render(request,'IncidentList.html',{'incidents':incidents})
@login_required
def IncidentCreated(request):
    if request.method=='POST':
        form=IncidentForm(request.POST,request.FILES)
        if form.is_valid():
            incident=form.save(commit=False)
            incident.user=request.user
            incident.save()
            return redirect('IncidentSeenHere')
    else:
        form=IncidentForm()
    return render(request,'IncidentCreated.html',{'form':form})
@login_required
def IncidentEdited(request,incident_id):
    incident=get_object_or_404(Incident,pk=incident_id,user=request.user)
    if request.method=='POST':
        form=IncidentForm(request.POST,request.FILES,instance=incident)
        if form.is_valid():
            incident=form.save(commit=False)
            incident.user=request.user
            incident.save()
            return redirect('IncidentSeenHere')
    else:
        form=IncidentForm(instance=incident)
    return render(request,'IncidentCreated.html',{'form':form})
@login_required
def incident_delete(request,incident_id):
    incident=get_object_or_404(Incident,pk=incident_id,user=request.user)
    if request.method=='POST':
        incident.delete()
        return redirect('IncidentSeenHere')
    return render(request,'Incident_delete_confirmation.html',{'incident':incident})


def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('IncidentSeenHere')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

def Quad(request):
    image_data = [
        ("/static/images/Quad/Prashant.jpg", "Prashant Pal, This is me the one who created this website. The gloomy guy who want to preserve this memories so that i will remember it no matter what."),
        ("/static/images/Quad/ashish2.jpg", "Ashish Patel (Mitra), One person in the group who study fucking too much. And the one who give Loan to the Entire Quad Squad. Mitra will be like agar isse bhidna hai to bhidna hi hai chahe wo truck kyu na ho. ATM WITH UNLIMITED BALANCE😂"),
        ("/static/images/Quad/bittu2.jpg", "Bittu Bahiya (Don), Bittu bahiya ke aage koi kuch nhi bol sakta kyuki bittu bahiya jo kahte hai wo hona hi hai. Agar bittu bahiya bole ki vasudev janeka to, even natural disaster can't stop Quad to go Vasudev. Bhale tum uske baad road pe kyu na aa jaye"),
        ("/static/images/Quad/deepak.jpg", "Deepak Jha, was a good Friend. Athlete guy mujhse running me koi nhi jeet sakta"),
        ("/static/images/Quad/anjali2.jpg", 'Anjali Upadhyay (Unofficial Member Of the Quad), You people dont even think of how much time i have wasted just to find this image of her. Agar ye bole ki tum galat hai, to galat hai accept it, if you dont then you will realise than you are sinner since the day you are born (Be wary of her) "MOST DANGEROUS PERSON"😨'),
        
        ]
    return render(request,'AboutQuad.html',{"image_data": image_data})