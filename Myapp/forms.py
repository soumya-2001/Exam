from django import forms
from Myapp.models import Category,Employee

class CategoryRegisterForm(forms.ModelForm):
    
    class Meta:
    
        model=Category
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Name"}),
        }
        
class EmployeeRegisterForm(forms.ModelForm):
    
    class Meta:
    
        model=Employee
        fields="__all__"
        
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Name"}),
            "mobile_number":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter your Phone Number"}),
            "place":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Place"}),
            "category_name":forms.Select(attrs={"class":"form-control"}),
            
        }
    
    