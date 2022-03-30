from django.shortcuts import render,redirect
from django.views.generic import View
from owner.forms import MobileForm
from owner.models import Mobile
# Create your views here.

class OwnerView(View):
    def get(self,request):
        form = MobileForm()
        return render(request,"addmobile.html",{"form":form})
    def post(self,request):
        form = MobileForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("allmobiles")
        else:
            return redirect("addmobile")

class MobileListView(View):
    def get(self,request):
        qs = Mobile.objects.all()
        return render(request,"mobilelist.html",{"mobiles":qs})

class DetailView(View):
    def get(self,request,*args,**kwargs):
        qs = Mobile.objects.get(id=kwargs.get("id"))
        return render(request,"mobiledetail.html",{"mobile":qs})




