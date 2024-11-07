from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField()

class Profile(models.Model):
    student = models.OneToOneField('university.Student',
                                   related_name='profile',
                                   on_delete=models.CASCADE)
    phone_number = models.IntegerField()

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Profesor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    courses = models.ManyToManyField('university.Course',
                                     related_name='profesors')
    
class UniversityClass(models.Model):
    course = models.ForeignKey('university.Course',
                               related_name='classes',
                               on_delete=models.CASCADE)
    students = models.ManyToManyField('university.Student',
                                      related_name='classes')

class Adress(models.Model):
    adress = models.TextField()

    student = models.ForeignKey('university.Student',
                                related_name='adress',
                                on_delete=models.CASCADE)
    
class Subject(models.Model):
    name = models.CharField(max_length=255)

    student = models.ForeignKey('university.Student',
                                related_name='subject',
                                on_delete=models.CASCADE)
    profesor = models.ManyToManyField('university.Profesor',
                                 related_name='subject',
                                 )