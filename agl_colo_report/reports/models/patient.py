from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField("Date of Birth")
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.dob.strftime('%Y-%m-%d')})"

    def natural_key(self):
        return (self.first_name, self.last_name)