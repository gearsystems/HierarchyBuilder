from django.contrib import admin
from orgtree.models import Employee
import autocomplete_light

autocomplete_light.autodiscover()
admin.site.register(Employee)

from orgtree.views import EmployeeCreate