from django.shortcuts import render
from .forms import PersonneRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method=='POST':
       fm =  PersonneRegistration(request.POST)#demande de l'utilisateur
    else:
               fm =  PersonneRegistration()
               if fm.is_valid():
                   nm = fm.cleaned_data['name']
                   em = fm.cleaned_data['email']
                   pw = fm.cleaned_data['password']
                   reg = User(name = nm, email= em, password = pw)
                   reg.save()
                   fm = PersonneRegistration()
    
    return render(request,'mon_AppAuto/addandshow.html',{'form':fm})
