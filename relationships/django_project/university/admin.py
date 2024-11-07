from django.contrib import admin
from university.models import Student, Profile, Course, Profesor, UniversityClass
# Register your models here.
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Profesor)
admin.site.register(UniversityClass)