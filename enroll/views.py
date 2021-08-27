from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

#This Function Is Add New Item And Show All Items.
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            #fm.save() 
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')
    else:
        fm = StudentRegistration()
    stud = User.objects.all() 

    return render(request,'enroll/addandshow.html',{'form':fm,'stu': stud})

#This For Delete function
def Delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#This is For Update Data
def Update_data(request ,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
         pi = User.objects.get(pk=id)
         fm = StudentRegistration(instance=pi)
    return render(request,'enroll/updatestudent.html' , {'form':fm})
