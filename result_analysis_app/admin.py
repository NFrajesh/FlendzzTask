from django.contrib import admin
from .models import StudentsMarks,Students
class StudentsAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno','dateofbirth']
class StudentsMarksAdmin(admin.ModelAdmin):
    list_display=['rollno','marks','grade']

admin.site.register(Students,StudentsAdmin)
admin.site.register(StudentsMarks,StudentsMarksAdmin)

# Register your models here.