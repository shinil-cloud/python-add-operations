from django.shortcuts import render,get_object_or_404,redirect
from app.models import Ert
from app.forms import ErtForm


# Create your views here.
def addErt(request):
    if(request.method=='POST'):
        ert_form=ErtForm(request.POST)
        if ert_form.is_valid():
            ert_form.save()
        return redirect('home')
            
    else:
        ert_form=ErtForm()
    return render(request,"ert/add_ert.html", {'form':ert_form })


def home(request):
    """post index view"""
    
    return render(request,"ert/homepage.html",{'objectlist':Ert.objects.all()})
 


 
