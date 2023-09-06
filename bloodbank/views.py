from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.db.models import Q

# Create your views here.
def home(request):
    blood_group = request.GET.get('bloodGroup') if request.GET.get('bloodGroup') != None else ''
    list = BloodSample.objects.filter(
        Q(blood_group__icontains=blood_group)
    )
    context = {"list": list}
    if request.method=='POST':
        blood_group=request.POST.get('donorBloodGroup')
        donorName=request.POST.get('donorName')

        blood_collect,completed=BloodSample.objects.get_or_create(blood_group=blood_group,doner=donorName)
        blood_collect.save()
        redirect('home')


    return render(request,'bloodbank/Blood.html',context)