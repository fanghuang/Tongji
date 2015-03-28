from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save


class Student(models.Model):
    user = models.OneToOneField('auth.User')
    student_id = models.IntegerField(primary_key=True)
    start_year = models.IntegerField()
    phone = models.CharField(max_length=11)

    @staticmethod
    def create_student(student_id, student_name, password, start_year):
        user = User.objects.create_user(username=student_id, password=password)
        user.first_name = student_name
        user.save()
        student = Student.objects.create(user=user, student_id=student_id, start_year = start_year)
        return student

    def __unicode__(self):
        return self.user.first_name



class Teacher(models.Model):
    PROFESSOR = "PROF"
    ASSOCIATE_PROFESSOR = "ASSO"
    ASSISTANT_PROFESSOR = "ASSI"
    INSTRUCTOR = "INST"

    POSITION_CHOICE = (
        (PROFESSOR, 'Professor'),
        (ASSOCIATE_PROFESSOR, 'Associate Professor'),
        (ASSISTANT_PROFESSOR, 'Assistant Professor'),
        (INSTRUCTOR, 'Instructor'),

    )
    name = models.CharField(max_length=5)
    position = models.CharField(max_length=2,
                                choices=POSITION_CHOICE,
                                null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True)

    def __unicode__(self):
        return self.name