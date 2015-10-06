from django.forms import ModelForm
from orgtree.models import Employee

"""Model Form to instantiate a new instance of Employee when given the below argurments"""
class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = ['name','title','email_address','phone','parent']