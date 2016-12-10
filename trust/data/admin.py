from django.contrib import admin
from data.models import Cause, Project, NGO, Consultant, Audit

#mention all the models to be viewed on the django admin panel
admin.site.register(Cause)
admin.site.register(Project)
admin.site.register(NGO)
admin.site.register(Consultant)
admin.site.register(Audit)

#add all the fields of the models you want to see on the django admin panel
#just add the word "Admin" to the model name
class CauseAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_amount')
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'total_amount', 'raised_amount', 'cause', 'ngo_id', 'zip', 'person_of_contact', 'summary', 'team_member_id')
class NGOAdmin(admin.ModelAdmin):
    list_display = ('name', 'person_of_contact', 'registration_code', 'address', 'website', 'team_member_id')
class ConsultantAdmin(admin.ModelAdmin):
    list_display = ('name')
class AuditAdmin(admin.ModelAdmin):
    list_display = ('date', 'report_id', 'consultant_id', 'project_id')