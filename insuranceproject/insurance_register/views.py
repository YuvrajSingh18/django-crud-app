from django.shortcuts import render, redirect
from .forms import InsuranceForm
from .models import Insurancerecord

# Create your views here.

def insurance_list(request):
    context = {'insurance_list':Insurancerecord.objects.all()}
    return render(request,"insurance_register/insurance_list.html",context)

def insurance_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = InsuranceForm()
        else:
            insurance = Insurancerecord.objects.get(pk=id)
            form = InsuranceForm(instance=insurance)
        return render(request,"insurance_register/insurance_form.html",{'form':form})
    else:
        if id==0:
            form = InsuranceForm(request.POST)
        else:
            insurance = Insurancerecord.objects.get(pk=id)
            form = InsuranceForm(request.POST,instance=insurance)
        if form.is_valid():
            form.save()
        return redirect('/insurance/list')

def insurance_delete(request,id):
    insurance = Insurancerecord.objects.get(pk=id)
    insurance.delete()
    return redirect('/insurance/list')