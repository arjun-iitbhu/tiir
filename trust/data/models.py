from django.db import models
from datetime import date

#KEYS NOT YET SPECIFIED
class Cause(models.Model):
    name = models.CharField(max_length = 60, blank = False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return "%s : %s" % (self.name, self.total_amount)

# CAUSES = Cause.objects.all()
# print CAUSES
#  #to retrieve all the added causes... NEEDS TO BE CHECKED....
#maybe server needs to be restarted to load it... need to be checked
#ALWAYS COMMENT IT OUT FIRST AND THEN SYNC THE DATABASE AND THEN UNCOMMENT IT

class Project(models.Model):
    title = models.CharField(max_length=128, blank=False,)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cause = models.CharField(max_length=30)
    ngo_id = models.IntegerField(blank=False)
    # cause = models.ForeignKey('Cause', on_delete = models.SET('uncategorised')) #FK... should be dynamic
    # ngo_id = models.ForeignKey('NGO', on_delete = models.SET('no_NGO_attached'))#FK #Can be a many-to-many relation?
    zip = models.IntegerField(blank = True)
    person_of_contact = models.CharField(max_length = 100)
    summary = models.CharField(max_length = 500, blank = False)
    team_member_id = models.IntegerField()#FK? #Can be a many-to-many relation?

    def __unicode__(self):
        return self.title

class NGO(models.Model):
    name = models.CharField(max_length = 200, blank = False)
    person_of_contact = models.CharField(max_length=100)
    registration_code = models.BigIntegerField(null = False)
    address = models.CharField(max_length = 200, blank = False)
    website = models.URLField()
    team_member_id = models.IntegerField()#FK? #Can be many-to-many relation?

    def __unicode__(self):
        return self.name

class Consultant(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

class Audit(models.Model):
    date = models.DateField(null=False)
    report_id = models.IntegerField(null = False)#report model needs to be added||Will there be more than one report for a project?
    consultant_id = models.IntegerField(null = False)
    project_id = models.IntegerField(null = False)

    def __unicode__(self):
        return "%s : %s" % (self.project_id, self.consultant_id)



