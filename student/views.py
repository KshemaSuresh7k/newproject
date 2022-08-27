
from datetime import date
from django.db import DataError
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import addteach,studreg,parreg,eventadd,leave
from django.contrib.auth import logout
#from .forms import registerform

# Create your views here.
def index(request):
    return render(request,'index.html')

def student(request):
    if request.method=="POST":
        sname=request.POST.get('sname')
        admno=request.POST.get('admno')
        department=request.POST.get('department')
        year=request.POST.get('year')
        course=request.POST.get('course')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contactno=request.POST.get('contactno') 

        studreg(sname=sname,admno=admno,department=department,year=year,course=course,email=email,password=password,contactno=contactno).save()
        return redirect('studentlogin')
    else:
        return render(request,'student.html')

def studentlogin(request):
    return render(request,'studentlogin.html')

def applyleave(request):
    if request.method=="POST":
        name=request.POST.get('name')
        admno=request.POST.get('admno')
        department=request.POST.get('department')
        date=request.POST.get('date')
        days=request.POST.get('days')
        reason=request.POST.get('reason')
        status=False
        leave(name=name,admno=admno,department=department,date=date,days=days,reason=reason,status=status).save()
    return render(request,'applyleave.html')

def teacherlogin(request):
    return render(request,'teacherlogin.html')

def teachlog(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
         
        cr=addteach.objects.filter(email=email,password=password)
        if cr:
           teacher_details=addteach.objects.get(email=email,password=password)
           id=teacher_details.id
           dept=teacher_details.department
           request.session['id']=id
           request.session['dept']=dept


           return redirect('teachhome')
        else:
            return render(request,'teacherlogin.html')
    else:

        return render(request,'index.html')



def parentlogin(request):
    return render(request,'parentlogin.html')

def parentreg(request):
    if request.method=="POST":
        username=request.POST.get('username')
        admno=request.POST.get('admno')
        department=request.POST.get('department')
        sname=request.POST.get('sname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        contactno=request.POST.get('contactno') 

        parreg(username=username,admno=admno,department=department,sname=sname,email=email,password=password,contactno=contactno).save()
        return redirect('parentlogin')
    else:
        return render(request,'parentreg.html')

def addevent(request):
    if request.method=="POST":
        eventname=request.POST.get('eventname')
        department=request.POST.get('department')
        date=request.POST.get('date')
        day=request.POST.get('day')
        time=request.POST.get('time')

        eventadd(eventname=eventname,department=department,date=date,day=day,time=time).save()
    return render(request,'addevent.html')

def studlog(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
         
        cr=studreg.objects.filter(email=email,password=password)
        if cr:
           user_details=studreg.objects.get(email=email,password=password)
           id=user_details.id
           email=user_details.email
           admno=user_details.admno
           dept=user_details.department
           request.session['admno']=admno
           request.session['dept']=dept

           request.session['id']=id
           request.session['email']=email
         
           return redirect('studhome')
        else:
            return render(request,'studentlogin.html')
    else:
        return render(request,'student.html')

def studhome(request):
    id=request.session['id']
    email=request.session['email']
    
    return render(request,'studhome.html',{'id':id,'email':email})

def parlog(request):
    if request.method=='POST':

        email=request.POST.get('email')
        password=request.POST.get('password')
         
        cr=parreg.objects.filter(email=email,password=password)
        if cr:
            user_details=parreg.objects.get(email=email,password=password)
            id=user_details.id
            email=user_details.email
            sname=user_details.sname
            admno=user_details.admno
            dept=user_details.department
            
            request.session['id']=id
            request.session['email']=email
            request.session['sname']=sname
            request.session['admno']=admno
            request.session['dept']=dept
        

            return redirect('parenthome')
   
        else:
            return render(request,'parentlogin.html')
    else:
        return render(request,'parentreg.html')

def parenthome(request):
    id=request.session['id']
    email=request.session['email']
    admno=request.session['admno']
    return render(request,'parenthome.html',{'id':id,'email':email,'admno':admno})

def teachhome(request):
    return render(request,'teachhome.html')

def noapprov(request):
    return render(request,'noapprov.html')

def viewleave(request):
    cr=leave.objects.all().filter(status=False)
    return render(request,'viewleave.html',{'cr':cr})

def approvleave(request,id):
    cr=leave.objects.get(pk=id)
    cr.status=True
    cr.save()
    return HttpResponseRedirect('/viewleave')

def delete(request,id):
    cr=leave.objects.get(pk=id)
    cr.delete()
    return HttpResponseRedirect('/teachhome')

def approvedleave(request):

#student leaveview
    #dept=request.session['admno']

    #cr = studreg.objects.filter(department=dept)
   # print(request.session['admno']) 
   # if request.session['dept']:
    dept=request.session['dept']
    cr = leave.objects.filter(department=dept)
    return render(request,"approvedleave.html",{'cr':cr})
    
    #cr=leave.objects.filter(admno=admno)
    #cr=leave.objects.all().filter(status=True)
    
   
def viewstudent(request):
    #print(cr)
    dept=request.session['dept']
    cr = studreg.objects.filter(department=dept)
    return render(request,'viewstudent.html',{'cr':cr})

def parentview(request):
    
    sname=request.session['sname']
    cr=studreg.objects.filter(sname=sname)

    return render(request,'parentview.html',{'cr':cr})
    

def logoutuser(request):
    logout(request)
    return redirect('index')


def detailleave(request):
     if request.method=='POST':
       choose_name = request.POST.get('admno')
       ce=leave.objects.filter(admno=choose_name,status=True)
       if ce:
        return render(request,"detailleave.html",{'ce':ce})
        
     return render(request,"detailleave.html")

def sapprovedleave(request):
    
    admno=request.session['admno']
    cr = leave.objects.filter(admno=admno)
    return render(request,'sapprovedleave.html',{'cr':cr})



def viewevent(request):
    dept=request.session['dept']
    cr = eventadd.objects.filter(department=dept)
    return render(request,'viewevent.html',{'cr':cr})


















