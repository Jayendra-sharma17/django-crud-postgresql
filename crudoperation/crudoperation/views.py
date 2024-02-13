from django.shortcuts import render
from crudoperation.models import EmpModel
from django.contrib import messages
from crudoperation.forms import Empforms

def showemp(request):
    showall=EmpModel.objects.all()
    return render(request,'index.html',{"data":showall})

def Insertemp(request):
    if request.method=="POST":
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('occuapation') and request.POST.get('salary') and request.POST.get('gender'):
            saverecord=EmpModel()
            saverecord.empname=request.POST.get('empname')
            saverecord.email=request.POST.get('email')
            saverecord.occuapation=request.POST.get('occuapation')
            saverecord.salary=request.POST.get('salary')
            saverecord.gender=request.POST.get('gender')
            saverecord.save()
            messages.success(request,'Employee is saved successfully!')
           
            return render(request,'insert.html')
        
    else:
            return render(request,"insert.html")    

 
def Editemp(request,id):
     editempobj=EmpModel.objects.get(id=id)
     return render(request,"Edit.html",{"EmpModel:":editempobj})


def  updateemp(request,id):
     Updateemp=EmpModel.objects.get(id=id)
     form=Empforms(request.POST,instance=Updateemp)
     if form.is_valid():
          form.save()
          messages.success(request,'record updated successfully')
     return render(request,'Edit.html',{"EmpModel":Updateemp})

def Delemp(request,id):
     delemployee=EmpModel.objects.get(id=id)
     delemployee.delete()
     showdata=EmpModel.objects.all()
     return render(request,"index.html",{"data":showdata})
 

          



