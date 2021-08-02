from django.db import models
from django.db.models.signals import post_save

class Students(models.Model):
    name=models.CharField(null=False,max_length=100)
    rollno=models.CharField(unique=True,null=False,max_length=15)
    dateofbirth=models.DateField(null=False,auto_now=False,auto_now_add=False)

    def __str__(self):
        return str(self.rollno)

class StudentsMarks(models.Model):
    rollno=models.ForeignKey(Students,on_delete=models.CASCADE,null=True,unique=True)
    marks=models.CharField(max_length=3,default='--')
    grade=models.CharField(max_length=2,default='--')
    
    def __str__(self):
        return str(self.rollno)
    
    def create_student_result(sender,instance,created,**kwargs):
        if created:
            StudentsMarks.objects.create(rollno=instance)
    post_save.connect(create_student_result,sender=Students)



