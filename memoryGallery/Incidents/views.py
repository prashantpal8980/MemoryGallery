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