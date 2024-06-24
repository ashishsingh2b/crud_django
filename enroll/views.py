from django.shortcuts import render,HttpResponseRedirect,redirect
from.forms import StudentRejistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == "POST":
        fm =StudentRejistration(request.POST)
        if fm.is_valid():
            #fm.save() direct method
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRejistration()
    else:
        fm=StudentRejistration()
    stud =User.objects.all()
    return render(request,'enroll/addandshow.html',{"form":fm,"stu":stud})

def update_data(request,id):
    if request.method == "POST":
        pi= User.objects.get(pk=id)
        fm = StudentRejistration(request.POST, instance=pi)
        if fm.is_valid():
           fm.save()
        
    else:
        pi =User.objects.get(pk=id)
        fm = StudentRejistration(instance=pi)
    return render(request,'enroll/updatestudent.html',{"form":fm})

def delete_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")