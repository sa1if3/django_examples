from django.shortcuts import render,redirect
from .forms import CompanyForm
from django.contrib import messages
# Create your views here.

def add_new_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Company added Succesfully')
                return redirect('add_new_company')
            except Exception as e:
                messages.error(request, str(e))
                return redirect('add_new_company')
    else:
        form = CompanyForm()
    return render(request, 'validation_app/company/add.html', {'form': form})

def home(request):
    return render(request,'validation_app/index.html')