from django.db import models

class Examiner(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    # center = models.ForeignKey('Center', on_delete=models.CASCADE)
    # qualifications = models.ManyToManyField('ExaminerQualification', blank=True)
    ## Qualification can be something like "Gastroenterologist", "Surgeon", "Nurse", "Physician", "Radiologist", "Other"
    ## ExaminerQualification links to Qualification and has date of qualification
    # Other stuff like experience bla bla bla