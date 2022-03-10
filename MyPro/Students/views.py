import os
import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps
from django.core.paginator import Paginator, EmptyPage

from MyPro.settings import BASE_DIR
from Students.models import (
	Student,
	Education,
	Family,
	Project,
	GovtID,
	Consultancy,
	Communication)
# Create your views here.


MODELS = apps.get_app_config('Students').get_models()

def home(request):
	return render(request, 'home_page.html')

def add_details(request):
	return render(request, 'add_student.html')

def get_next_id(model_name):
	try:
		return eval(model_name).objects.last().id + 1
	except:
		return 1

def add_student(request):
	try:
		student_obj = Student.objects.create(id=get_next_id('Student'),
			first_name=request.POST.get('First_Name'),
			last_name=request.POST.get('Last_Name'),
			mail=request.POST.get('Mail'),
			gender=request.POST.get('Gender'),
			phone=request.POST.get('Phone'),
			dob=(datetime.datetime.strptime(request.POST.get('Dob'), '%Y-%m-%d').date()),
			surname=request.POST.get('Surname'),
			address=request.POST.get('Address')
			)
		image_info = request.FILES.get('Image')
		if image_info:
			student_obj.image = image_info
		student_obj.save()
	except:
		return HttpResponseRedirect('/add_details')
	
	return render(request, 'add_education.html', {'student_mail': request.POST.get('Mail')})

def add_education(request):
	try:
		student_obj = Student.objects.get(mail=request.POST.get('Mail'))
	except:
		return HttpResponseRedirect('/add_details/')
	
	try:
		edu_obj = Education.objects.create(id=get_next_id('Education'),
			degree=request.POST.get('Degree'),
			student_name=student_obj,
			pass_out_year=int(request.POST['Pass_out_year'].split('-')[0]),
			percentage=float(request.POST.get('Percentage')),
			college_name=request.POST.get('College_name'),
			university_name=request.POST.get('University_name'),
			location=request.POST.get('Location')
			)
		edu_obj.save()
	except:
		return HttpResponseRedirect('/add_details/')

	if request.POST.get('Add_More'):
		return render(
			request, 'add_education.html', {'student_mail': request.POST.get('Mail')})

	return render(
		request, 'add_govt_details.html', {'student_mail': request.POST.get('Mail')})

def add_govtId(request):
	try:
		student_obj = Student.objects.get(mail=request.POST.get('Mail'))
	except:
		return HttpResponseRedirect('/add_details/')

	try:
		govt_id_obj = GovtID.objects.create(id=get_next_id('GovtID'),
		student_name=student_obj,
			id_type=request.POST.get('Id_type'),
			id_number=request.POST.get('Id_num')
			)
		image_info = request.FILES.get('Image')
		if image_info:
			govt_id_obj.image = image_info
		govt_id_obj.save()
	except:
		return HttpResponseRedirect('/add_details/')
		
	if request.POST.get('Add_More'):
		return render(
			request, 'add_govt_details.html', {'student_mail': request.POST.get('Mail')})

	return render(request, 'add_consultancy.html', {'student_mail': request.POST.get('Mail')})

def add_consultancy(request):
	try:
		student_obj = Student.objects.get(mail=request.POST.get('Mail'))
	except:
		return HttpResponseRedirect('/add_details/')
	
	try:
		consultancy_obj = Consultancy.objects.create(id=get_next_id('Consultancy'),
			student_name=student_obj,
			name=request.POST.get('Name'),
			start_date=request.POST.get('Start_date'),
			end_date=request.POST.get('End_date'),
			location=request.POST.get('Location')
			)
		consultancy_obj.save()
	except:
		return HttpResponseRedirect('/add_details/')

	if request.POST.get('Add_More'):
		render(request, 'add_consultancy.html', {'student_mail': request.POST.get('Mail')})
	return render(request, 'add_communication.html', {'student_mail': request.POST.get('Mail')})

def add_communication(request):
	try:
		student_obj = Student.objects.get(mail=request.POST.get('Mail'))
	except:
		return HttpResponseRedirect('/add_details/')

	try:
		communication_obj = Communication.objects.get(student_name=student_obj)
		communication_obj.skype_id = request.POST.get('Skype_id')
		communication_obj.linked_in = request.POST.get('Linked_in')
		communication_obj.save()
	except:
		communication_obj = Communication.objects.create(id=get_next_id('Communication'),
			student_name=student_obj,
			skype_id=request.POST.get('Skype_id'),
			linked_in=request.POST.get('Linked_in')
			)
		communication_obj.save()

	return HttpResponseRedirect('/home/')

def dump_to_csv(request):
	try:
		for model_name in MODELS:
			try:
				model_name.objects.to_csv('{}/BACKUP_CSV/{}_info.csv'.format(
					BASE_DIR, model_name.__name__))
			except:
				continue
	except:
		return HttpResponseRedirect('/add_details/')
	return HttpResponse("Data Dumped into CSV files succesfully...")

def load_from_csv(request):
	try:
		for model_name in MODELS:
			try:
				model_name.objects.from_csv('{}/BACKUP_CSV/{}_info.csv'.format(BASE_DIR, model_name.__name__))
			except:
				continue
	except:
		return HttpResponseRedirect('/add_details/')

	return HttpResponse("Data Dumped into Database from CSV files succesfully...")

def drop_all_tables(request):
	import psycopg2
	from psycopg2 import Error
	try:
	    connection = psycopg2.connect(user="postgres",
	                                  password="admin123",
	                                  host="localhost",
	                                  port="5432",
	                                  database="postgres")

	    cursor = connection.cursor()
	    # SQL query to create a new table
	    drop_query = '''DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;'''
	    # Execute a command: this creates a new table
	    cursor.execute(drop_query)
	    return HttpResponse("Table created successfully in PostgreSQL ")

	except (Exception, Error) as error:
	    return HttpResponse("Error while connecting to PostgreSQL", error)

def show_students(request):
	student_obj = Student.objects.all()
	p = Paginator(student_obj, 5)
	page_num = request.GET.get('page', 1)
	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)
	context = {'items' : page}
	return render (request, 'students.html', context)

def search_mail(request):
	return HttpResponse("Success....")