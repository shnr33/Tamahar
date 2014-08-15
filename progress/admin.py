from django.contrib import admin
from progress.models import Child,Section,SubSection,AgeRange,Question,Assessment,Response,Curriculum
# Register your models here.

class ChildAdmin(admin.ModelAdmin):
	search_fields = ['name']

class AssessmentAdmin(admin.ModelAdmin):
	list_filter = ['date']
	search_fields = ['child','date']

class ResponseAdmin(admin.ModelAdmin):
	search_fields = ['question','assessment']



admin.site.register(Child,ChildAdmin)
admin.site.register(Curriculum)
admin.site.register(Section)
admin.site.register(SubSection)
admin.site.register(AgeRange)
admin.site.register(Question)
admin.site.register(Assessment,AssessmentAdmin)
admin.site.register(Response,ResponseAdmin)