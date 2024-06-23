import simpy
import random


wait_times = []

class Department(object):
    def __init__(self, env, emp_available, equip_available):
        
        self.env = env
        self.no_of_patients = 0
        # services_available > service_type(key) > (values in form of dict)emp_needed + equip_needed + min_time_taken + max_time_taken
        
        self.emp = {}
        for emp_type, num_emp in emp_available.items():
            self.emp[emp_type] = simpy.Resource(env, num_emp)
        # {type1:num1, type2:num2, ...}

        self.equip = {}
        for equip_type, num_equip in equip_available.items():
            self.equip[equip_type] = simpy.Resource(env, num_equip)


    # def initiate_service(self, patient, service_type):
    #     yield self.env.timeout(random.randint(self.services_available[service_type]['min_time_taken'], self.services_available[service_type]['max_time_taken']))
        

        
    # def check_ecg(self, patient):
    #     yield self.env.timeout(random.randint(10,15))

    # def initial_diagnosis(self, patient):
    #     yield self.env.timeout(random.randint(3, 17))
    
    # def tmt_investigation(self, patient):
    #     yield self.env.timeout(random.randint(10,20))

