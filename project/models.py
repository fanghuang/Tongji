from django.db import models
from django.utils.translation import ugettext_lazy as _



class Project(models.Model):
    DEPARTMENT = "A"
    UNIVERSITY = "B"
    PROVINCE = "C"
    NATION = "D"
    TYPE_CHOICES = (
        (DEPARTMENT, _('A. Department')),
        (UNIVERSITY, _('B. University')),
        (PROVINCE, _('C. Province')),
        (NATION, _('D. Nation')),
    )

    title = models.CharField(max_length=50)
    leader = models.ForeignKey("account.Student", related_name="leading_project")
    description = models.TextField()
    members = models.ManyToManyField('account.Student', related_name="involved_project", db_constraint=False)
    teacher = models.ForeignKey('account.Teacher')
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    approved_time = models.DateTimeField(null=True)
    finished_time = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.title


class Mark(models.Model):
    project = models.ForeignKey('project.Project')
    comment = models.TextField()
    credit = models.IntegerField()
    # TODO
    # stage
