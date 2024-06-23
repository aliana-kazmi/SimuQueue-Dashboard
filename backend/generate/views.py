from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from generate.services.simulate_services import generate_data
from generate.models import Department, Service, Equipment, Employee, Simulator_Meta_Data
from django.forms.models import model_to_dict
# Create your views here.

def avg_waiting_time_patient_data(request):
    pass

def avg_waiting_time_dept_data(request, num_doctors, num_nurses, num_technicians, sim_time, seed):
    res = {}
    meta_data = {}
    dept_list = Department.objects.all().order_by('pk')
    
    for dept in dept_list:
        dept_name = dept.name
        dept_to_be_simulated = Department.objects.get(name = dept_name)
        services = Service.objects.filter(belongs_to=dept_to_be_simulated)
        equipments = Equipment.objects.filter(dept=dept_to_be_simulated)
        
        meta_data_obj = Simulator_Meta_Data.objects.filter(dept=dept_to_be_simulated, num_doctors=num_doctors,num_technicians=num_technicians, num_nurses=num_nurses, sim_time=sim_time, seed=seed)[0]
        if not meta_data_obj:
            meta_data_obj = Simulator_Meta_Data.objects.create(dept=dept_to_be_simulated, num_doctors=num_doctors,num_technicians=num_technicians, num_nurses=num_nurses, sim_time=sim_time, seed=seed)
        
        meta_data = model_to_dict(meta_data_obj)   

        services_needed = []
        for service in services:
            services_needed.append(model_to_dict(service))

        equip_available = {}
        for equipment in equipments:
            equip_available[equipment.name]=equipment.number

        emp_available = {
            'doctors': num_doctors,
            'nurses' :num_nurses,
            'technicians': num_technicians
        }
        
        data = generate_data(emp_available, equip_available, services_needed, meta_data)
        
        res[dept_name] = data
        
        labels = list(res.keys())
        data_field = list(res.values())
    return JsonResponse({
        'labels':labels,
        'data':data_field,
    },
    
    )