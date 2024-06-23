from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Equipment)
admin.site.register(Service)
admin.site.register(Simulator_Meta_Data)
admin.site.register(Simulator_Data)