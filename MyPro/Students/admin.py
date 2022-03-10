from django.contrib import admin

from Students.models import Student, Education, Family, Project, GovtID, Consultancy, Communication
# Register your models here.

admin.site.register(Student)
admin.site.register(Education)
admin.site.register(Family)
admin.site.register(Project)
admin.site.register(GovtID)
admin.site.register(Consultancy)
admin.site.register(Communication)