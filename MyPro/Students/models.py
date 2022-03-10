import datetime

from postgres_copy import CopyManager
from django.db import models

from MyPro.settings import BASE_DIR
# Create your models here.

class Student(models.Model):
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 25)
	mail = models.EmailField(max_length=30)
	image = models.ImageField(upload_to='{}/Student_Photos/'.format(BASE_DIR), null = True,blank = True)
	gender = models.CharField(max_length = 25)
	phone = models.CharField(unique=True, max_length=100)
	dob = models.DateField()
	surname = models.CharField(max_length=25)
	address = models.CharField(max_length=300)
	objects = CopyManager()

	def __str__(self):
		return self.first_name

class Education(models.Model):
	student_name = models.ForeignKey(Student,on_delete=models.CASCADE)
	degree = models.CharField(max_length = 25)
	pass_out_year = models.IntegerField()
	percentage = models.DecimalField(max_digits=5, decimal_places=2)
	college_name =  models.CharField(max_length = 100)
	university_name =  models.CharField(max_length = 100)
	location =  models.CharField(max_length = 25)
	objects = CopyManager()

	def __str__(self):
		return self.student_name.first_name

class Family(models.Model):
	student_name = models.ForeignKey(Student,on_delete=models.CASCADE)
	name = models.CharField(max_length = 25)
	occupation = models.CharField(max_length = 25)
	relation = models.CharField(max_length = 25)
	gender = models.CharField(max_length = 25)
	objects = CopyManager()

	def __str__(self):
		return self.student_name.first_name

class Project(models.Model):
	student_name = models.ForeignKey(Student,on_delete=models.CASCADE)
	project_name = models.CharField(max_length = 100)
	start_date = models.CharField(max_length=100)
	end_date = models.CharField(max_length = 100 ,default="in progress")
	team_size = models.IntegerField(default=5)
	objects = CopyManager()

	def __str__(self):
		return self.student_name.first_name

class GovtID(models.Model):
	student_name = models.ForeignKey(Student,on_delete=models.CASCADE)
	id_type = models.CharField(max_length = 100)
	id_number = models.CharField(max_length = 100,unique=True)
	image = models.ImageField(upload_to='{}/GovtID_Photos/'.format(BASE_DIR), null=True, blank=True)
	objects = CopyManager()

	def __str__(self):
		return self.student_name.first_name

class Consultancy(models.Model):
	student_name = models.ForeignKey(Student,on_delete=models.CASCADE)
	name = models.CharField(max_length = 100)
	start_date = models.CharField(max_length=100)
	end_date = models.CharField(max_length = 25 ,default="working")
	location =  models.CharField(max_length = 100)
	objects = CopyManager()

	def __str__(self):
		return self.student_name.first_name

class Communication(models.Model):
	student_name = models.ForeignKey(Student,on_delete=models.CASCADE)
	skype_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
	linked_in = models.CharField(max_length=100, null=True, blank=True, unique=True)
	objects = CopyManager()

	def __str__(self):
		return self.student_name.first_name

