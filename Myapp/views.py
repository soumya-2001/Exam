from django.shortcuts import render,redirect
from django.views.generic import View

from Myapp.models import Category,Employee
from Myapp.forms import CategoryRegisterForm,EmployeeRegisterForm

# Create your views here.


class CategoryCreateView(View):
    
    def get(self,request,*args, **kwargs):
        
        form=CategoryRegisterForm()
        return render(request,"category_register.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        
        form=CategoryRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("category-create")
        return render(request,"category_register.html",{"form":form})
    
class EmployeeCreateView(View):
    
    def get(self,request,*args, **kwargs):
        
        form=EmployeeRegisterForm
        return render(request,"employee_register.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        
        form=EmployeeRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
        return render(request,"employee_register.html",{"form":form})
            
# class EmployeeListView(View):
    
#     def get(self,request,*args, **kwargs):
        
#         qs=Employee.objects.all()
#         return render(request,"employee_list.html",{"data":qs})
    
class EmployeeListView(View):
    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        cator=Category.objects.all()
        cat = request.GET.get("category")
        print(cat)
        if cat:
            qs = qs.filter(category_name__name = cat)
            
        return render(request,"employee_list.html",{"data":qs,"cat":cator})
    
class EmployeeDetailView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,"employee_detail.html",{"data":qs})
    
class EmployeeUpdateView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        form=EmployeeRegisterForm(instance=qs)
        return render(request,"employee_update.html",{"form":form})
    
    def post(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        form=EmployeeRegisterForm(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
        return render(request,"employee_update.html",{"form":form})
    
class EmployeeDeleteView(View):
    
    def get(self,request,*args, **kwargs):
        
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id).delete()
        return redirect("employee-list")
    

    
    

        


            
