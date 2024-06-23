from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=60)
    hod = models.CharField(max_length=70)

    def __str__(self):
        return str(self.name) + " Department"

class Employee(models.Model):
    type = models.CharField(max_length=70)
    number = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.type) + " from Department " + self.dept.name

class Equipment(models.Model):
    name = models.CharField(max_length=35,default="")
    brand = models.CharField(max_length=80)
    number = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.brand) + " " + str(self.name) + " from " + self.dept.name + " Department"

class Service(models.Model):
    type = models.CharField(max_length=60)
    min_time_taken = models.DecimalField(max_digits=7,decimal_places=2)
    max_time_taken = models.DecimalField(max_digits=7,decimal_places=2)
    is_compulsory = models.BooleanField(default=False)
    belongs_to = models.ForeignKey(Department, on_delete=models.CASCADE)
    assigned_staff = models.ManyToManyField(Employee)
    equipment_required = models.ManyToManyField(Equipment)

    def __str__(self):
        return str(self.type) + " in " + self.belongs_to.name + " Department"
    

class Simulator_Meta_Data(models.Model):
    dept = models.ForeignKey(Department,on_delete=models.CASCADE,default=0)
    num_doctors = models.IntegerField()
    num_nurses = models.IntegerField()
    num_technicians = models.IntegerField()
    sim_time = models.DecimalField(max_digits=7, decimal_places=2)
    seed = models.IntegerField()

    def __str__(self):
        return "Meta Data for Dept " + str(self.dept.name) + ": " + str(self.id)
    
    class Meta:
        verbose_name = "Simulated Meta Data"
        verbose_name_plural = "Simulated Meta Data"


class Simulator_Data(models.Model):
    id = models.CharField(primary_key=True,max_length=30)
    type_of_queue = models.CharField(max_length=30)
    no_of_patients = models.BigIntegerField()
    last_simulated = models.DateTimeField(auto_now=True)
    avg_time_per_patient = models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    meta_data = models.ForeignKey(Simulator_Meta_Data, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "Simulator Data for dept " + str(self.meta_data.dept.name) + ": " + str(self.id)
    
    class Meta:
        verbose_name = "Simulated Data"
        verbose_name_plural = "Simulated Data"