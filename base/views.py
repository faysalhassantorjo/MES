from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Category,Doctors

# Create your views here.
def home(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'base/index/index.html',context)

def doctorList(request, pk):
    category = get_object_or_404(Category, id=pk)
    doclist = Doctors.objects.filter(category=category)
    context = {'category': category, 'doclist': doclist}
    return render(request, 'base/Doctorlist/doctorList.html', context)

def docDetails(request, pk):
    doc = get_object_or_404(Doctors, id=pk)
    context = {'doctor': doc}
    return render(request, 'base/Doctordetails/doc.html', context)
def selectdate(request):
    return render(request,'base/Calendar/cal.html')
