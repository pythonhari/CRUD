from django.shortcuts import render
from .models import Employee
from .forms import Employeeform,Updateform,Deleteform
from django.http import HttpResponse

# Create your views here.
def retrieveview(request):
    employees=Employee.objects.all()
    return render(request,'index.html',{'employees':employees})
def createview(request):
    if request.method=='POST':
        form=Employeeform(request.POST)
        if form.is_valid():
            eno1=request.POST.get('eno')
            ename1=request.POST.get('ename')
            esal1=request.POST.get('esal')
            eaddr1=request.POST.get('eaddr')
            ephno1=request.POST.get('ephno')
            data=Employee(
                 eno=eno1,
                 ename=ename1,
                 esal=esal1,
                 eaddr=eaddr1,
                 ephno=ephno1
            )
            data.save()
            form=Employeeform()
            return render(request,'create.html',{'form':form})
        else:
             return HttpResponse("Invalid data")
    form = Employeeform()
    return render(request, 'create.html', {'form': form})


def updateview(request):
    if request.method=="POST":
        uform=Updateform(request.POST)
        if uform.is_valid():
            eno1=request.POST.get('eno')
            esal1=request.POST.get('esal')
            udata=Employee.objects.filter(eno=eno1)
            if udata:
                udata.update(esal=esal1)
                uform=Updateform()
                return render(request,'update.html',{'uform':uform})
            else:
                return HttpResponse("Invalid eno")
        else:
            return HttpResponse("Invalid details")
    uform=Updateform()
    return render(request,'update.html',{'uform':uform})

def deleteview(request):
    if request.method=="POST":
        dform=Deleteform(request.POST)
        if dform.is_valid():
            eno1=request.POST.get('eno')
            ddata=Employee.objects.filter(eno=eno1)
            if ddata:
                ddata.delete()
                dform=Deleteform()
                return render(request,"delete.html",{'dform':dform})
            else:
                return HttpResponse("Invalid id")
        else:
            return HttpResponse("Invalid data")
    dform = Deleteform()
    return render(request, "delete.html", {'dform': dform})







