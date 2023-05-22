from django.shortcuts import render
from .forms import employeeForm
from .models import employee
from .forms import SearchForm
# Create your views here.
def show(request):
    return render(request,'home.html')

def signup(request):
    form = employeeForm(request.POST or None)
    if form.is_valid():
        fname = form.cleaned_data['first_name']
        lname = form.cleaned_data['last_name']
        mail = form.cleaned_data['email_number']
        pword = form.cleaned_data['password']
        phone = form.cleaned_data['phone_number']
        jtitle = form.cleaned_data['job_title']
        p = employee(first_name=fname,last_name=lname,email_number=mail,password=pword,phone_number=phone,job_title=jtitle)
        p.save()
        return render(request,'index.html',{'message':'Employee Registered sucesssfully'})

    context = {
        'form':form,
        
    }

    return render(request,'signup.html',context)
def registered(request):
    title = 'List of registered employee'
    queryset = employee.objects.all()
    context = {
        'title':title,
        'queryset':queryset
    }

    return render(request,'registered.html',context)

def Search(request):
    title = 'Search for Employee'
    form = SearchForm(request.POST or None)
    if form.is_valid():
        fname = form.cleaned_data['first_name']
        qeuryset = employee.objects.filter(first_name=fname)

        context = {
            'title':title,
            'queryset':qeuryset
        }
        return render(request,'registered.html',context)
    context = {
        'title':title,
        'form':form
    }

    return render(request,'search.html',context)

def Delete(request):
    title = 'Deleted Employee'
    form = SearchForm(request.POST or None)
    if form.is_valid():
        fname = form.cleaned_data['first_name']
        qeuryset = employee.objects.filter(first_name=fname).delete()

        
        return render(request,'deleted.html',{'message':'Student deleted Sucessfully'})
    context = {
        'title':title,
        'form':form
    }

    return render(request,'delete.html',context)
