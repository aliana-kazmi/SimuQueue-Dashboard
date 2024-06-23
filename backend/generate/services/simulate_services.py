import random
import statistics
import simpy
from generate.services.generate_resources import wait_times, Department

patient_count = 0
def go_to_dept(env, patient, services_needed:list, dept):
    arrival_time = env.now #patient arrives at dept
    # print(f"patient {patient_count} arrived at {arrival_time}")
    req_arr = []
    for service in services_needed:
        i=0
        j=0
        
        for emp in service['assigned_staff']:
            emp_type = emp.type
            request = dept.emp[emp_type].request()
            # wait for access
            yield request
            i+=1
            req_arr.append(request)
        print(f"Employees engaged for patient {patient} in {service['type']} & emp {emp_type}")

        # generate request for equipment
        for equipment in service['equipment_required']:
            equipment_type = equipment.name
            request = dept.equip[equipment_type].request()
            # wait for access
            yield request
            i+=1
            req_arr.append(request)
        
        print(f"Equipments engaged for patient {patient} & equip {equipment_type} \n Process has started")
        # service underway
        yield dept.env.timeout(random.randint(service['min_time_taken'], service['max_time_taken']))
        
        # releasing employee resources
        for emp_type in service['assigned_staff']:
            dept.emp[emp_type.type].release(req_arr[j])
            j+=1

        # releasing equipment resources
        for equip_type in service['equipment_required']:
            equip_name = equip_type.name
            dept.equip[equip_name].release(req_arr[j])
            j+=1

        print(f"Patient {patient} released equip and emp")

# wait times calculation
        wait_times.append(env.now - arrival_time)

        # request = resource.request()  # Generate a request event
        # yield request                 # Wait for access
        # yield env.timeout(1)          # Do something
        # resource.release(request)     # Release the resource



def patient_arrivals(env, emp_available, equip_available, services_needed):
    dept = Department(env, emp_available, equip_available)
    
    patient_count = 0
    # Day started with 15 patients in beginning
    for patient in range(15):
        
        print(f"patient {patient_count} goes to dept")
        env.process(go_to_dept(env, patient, services_needed, dept))
        patient_count+=1
    
        # patient arrival every 20 
        while True:
            yield env.timeout(0.2)
            # patient production
            patient+=1
            patient_count+=1
            print(f"patient {patient_count} goes to dept")
            env.process(go_to_dept(env, patient, services_needed, dept))



# resource number validation to be put in form
# checking if input is valid or not

def validate_resource_input(num_doctors, num_nurses, num_technicians):
    params = [num_doctors, num_nurses, num_technicians]
    if all(str(i).isdigit() for i in params):  # Check input is valid
        params = [int(x) for x in params]
    else:
        print(
            "Could not parse input. The simulation will use default values:",
            "\n1 doctor, 1 nurse 1 technician.",
        )
        params = [1, 1, 1]
    return params


def calculate_wait_time(avg_wait):
    minutes, frac_minutes = divmod(avg_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def generate_data(emp_available, equip_available, services_needed,meta_data):
  # Setup
  RANDOM_SEED = meta_data.seed
  random.seed(RANDOM_SEED)
  SIMULATION_TIME = meta_data.sim_time
  # Run the simulation
  env = simpy.Environment()
  env.process(patient_arrivals(env, emp_available, equip_available, services_needed))
  env.run(until=SIMULATION_TIME)

  # View the results
  print(wait_times)
  avg_wait = statistics.mean(wait_times)
  return {'avg_wait':avg_wait, 'patient_count':patient_count}


#   mins, secs = calculate_wait_time(avg_wait)
#   print(
#       "Running simulation...",
#       f"\nThe average wait time is {mins} minutes and {secs} seconds with {len(wait_times)} patients.",
#   )
#   print("Waiting times are:\n")
#   for wait_time in wait_times:
#       print(f'{wait_time}')
