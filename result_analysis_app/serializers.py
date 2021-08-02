from rest_framework import serializers
from .models import StudentsMarks,Students

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class StudentsMarksSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentsMarks
        fields = '__all__'



