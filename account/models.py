from django.db import models

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField('auth.User')
    student_id = models.IntegerField()
    start_year = models.IntegerField()
    phone = models.CharField(max_length=11)


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

    position = models.CharField(max_length=2,
                                choices=POSITION_CHOICE,
                                default=PROFESSOR)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
