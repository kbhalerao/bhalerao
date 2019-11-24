from django.db import models
import datetime

# Create your models here.

class Student(models.Model):
    
    name = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name

class Menu(models.Model):

    ems = models.URLField(help_text="Edison Menu")
    cb = models.URLField(help_text="Carrie Busey Menu")


class PlanManager(models.Manager):
    
    def create_lunch_plan_for_week_starting(self, start):
        
        for s in Student.objects.all():
            for i in range(0,5):
                try:
                    Plan.objects.get(student=s, 
                                     date=(start+datetime.timedelta(i)).date())
                except Plan.DoesNotExist:
                    Plan.objects.create(student=s, 
                                        date=(start+datetime.timedelta(i)).date(), 
                                        lunch="C")
                    
            


class Plan(models.Model):

    CHOICES = (('H', 'Hot Lunch'), ('C', 'Cold Lunch'))
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    lunch = models.CharField(max_length=1, choices=CHOICES)
    objects = PlanManager()
    
    def __str__(self):
        return "{}: {} - {}".format(self.date, 
                                    self.student.name, 
                                    self.get_lunch_display())

