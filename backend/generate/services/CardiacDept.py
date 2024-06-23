import simpy
import random
import statistics

wait_times = []

class CardiacDept(object):
    def __init__(self, env, num_doctors,num_nurses, num_technicians):
        self.env = env
        self.doctor = simpy.Resource(env, num_doctors)
        self.nurse = simpy.Resource(env, num_nurses)
        self.technician = simpy.Resource(env, num_technicians)


    def check_bp(self, patient):
        yield self.env.timeout(random.randint(3,7))

    def check_ecg(self, patient):
        yield self.env.timeout(random.randint(10,15))

    def initial_diagnosis(self, patient):
        yield self.env.timeout(random.randint(3, 17))
    
    def tmt_investigation(self, patient):
        yield self.env.timeout(random.randint(10,20))



def go_to_dept(env, patient, cardiac_dept):
    arrival_time = env.now #patient arrives at dept

    with cardiac_dept.nurse.request() as request:
        yield request
        print('here 1 '+ env.now)
        yield env.process(cardiac_dept.check_bp(patient))
        
        print('here 2 '+ env.now)
        yield env.process(cardiac_dept.check_bp(patient))

        
    with cardiac_dept.technician.request() as request:
        yield request
        yield env.process(cardiac_dept.check_ecg(patient))

    with cardiac_dept.doctor.request() as request:
        yield request
        yield env.process(cardiac_dept.initial_diagnosis(patient))

    if random.choice([True, False]):
        with cardiac_dept.technician.request() as request:
            yield request
            yield env.process(cardiac_dept.tmt_investigation(patient))

    wait_times.append(env.now - arrival_time)


def run_cardiac_dept(env, num_doctors=1,num_nurses=1, num_technicians=1):
    cardiac_dept = CardiacDept(env, num_doctors,num_nurses, num_technicians)
    for patient in range(5):
        env.process(go_to_dept(env, patient, cardiac_dept))

    while True:
        yield env.timeout(0.20)

        patient+=1
        env.process(go_to_dept(env, patient, cardiac_dept))

def calculate_wait_time(wait_times):
    avg_wait = statistics.mean(wait_times)
    minutes, frac_minutes = divmod(avg_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def validate_resource_input(num_doctors, num_nurses, num_technicians):
    # checking if input is valid or not

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

def generate_data(num_doctors, num_nurses, num_technicians):
  # Setup
  random.seed(42)

  # Run the simulation
  env = simpy.Environment()
  env.process(run_cardiac_dept(env, num_doctors, num_nurses, num_technicians))
  env.run(until=90)

  # View the results
  mins, secs = calculate_wait_time(wait_times)
  print(
      "Running simulation...",
      f"\nThe average wait time is {mins} minutes and {secs} seconds with {len(wait_times)} patients.",
  )
  print("Waiting times are:\n")
  for wait_time in wait_times:
      print(f'{wait_time}')
