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

    STATUS_CHOICES = (
        ("PENDING", _('A. PENDING')),
        ("APPROVED", _('B. APPROVED')),
        ("REJECTED", _('C. REJECTED')),
    )  

    title = models.CharField(max_length=50)
    leader = models.ForeignKey("account.Student", related_name="leading_project")
    description = models.TextField()
    members = models.ManyToManyField('account.Student', related_name="involved_project", db_constraint=False)
    teacher = models.ForeignKey('account.Teacher')
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    #TODO do we need approved_time & finished_time
    approved_time = models.DateTimeField(null=True)
    finished_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('project_detail', args=[str(self.id)])


class Mark(models.Model):
    project = models.ForeignKey('project.Project')
    comment = models.TextField()
    credit = models.IntegerField()
    # TODO
    # stage
