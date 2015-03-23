from django.db import models


class Project(models.Model):
    SCHOOL = "A"
    UNIVERSITY = "B"
    PROVINCE = "C"
    NATION = "D"
    TYPE_CHOICES = (
        (SCHOOL, 'A. School'),
        (UNIVERSITY, 'B. University'),
        (PROVINCE, 'C. Province'),
        (NATION, 'D. Nation'),
    )

    title = models.CharField(max_length=50)
    description = models.TextField()
    leader = models.ForeignKey("account.Student", related_name="leading_project")
    members = models.ManyToManyField('account.Student', related_name="involved_project")
    teacher = models.ForeignKey('account.Teacher')
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    approved_time = models.DateTimeField()
    finished_time = models.DateTimeField()


class Mark(models.Model):
    project = models.ForeignKey('project.Project')
    comment = models.TextField()
    credit = models.IntegerField()
    # TODO
    # stage
