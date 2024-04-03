from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .forms import CustomerUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Department
from .models import Student
from .forms import StudentForm



# Create your views here.
def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')



def register(request):

    if request.method =='POST':
        form=CustomerUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect('login')
    else:
            form=CustomerUserForm()
    return render(request,'register.html',{'form': form})

def login_view(request):
     if request.method=='POST':
          form=AuthenticationForm(data=request.POST)
          if form.is_valid():
               #log the user in
               user=form.get_user()
               login(request,user)
               return HttpResponseRedirect('dashboard') #redirect to home
     else:
          form=AuthenticationForm()
     return render(request,'login.html',{'form':form})

def dashboard_view(request):
     return render(request,'dashboard.html')


def department_view(request):
     dict_dept={
        'dept':Department.objects.all()
     }
     return render(request,'department.html',dict_dept)

def student(request):
     students=Student.objects.all()
     return render(request,'student.html',{'students':students})

def add_student(request):
     if request.method=='POST':
          form=StudentForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('student')
     else:
        form=StudentForm()
     return render(request,'add_student.html',{'form': form})