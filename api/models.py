from django.db import models

# Create your models here.


class Employee(models.Model):

    emp_id=models.CharField(max_length=200)

    name=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    def __str__(self):

        return self.name

class Task(models.Model):

    title=models.CharField(max_length=200)

    description=models.CharField(max_length=200)

    completed_date=models.DateTimeField()

    assigned_date=models.DateTimeField()

    status=models.CharField(max_length=200)

    employee_object=models.ForeignKey(Employee,on_delete=models.CASCADE)

    def _str_(self):

        return self.title