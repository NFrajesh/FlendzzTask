"""Flendzz_Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
#<--------------------------------student-details------------------>
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.Home,name="students"),
    path('student/<int:pk>/', views.Detail,name="student detail"),
    path('student/add-student', views.AddStudent,name="add student"),
    path('student/update/<int:pk>/', views.Update,name="update student"),


#<--------------------------------student-Marks----------------------------->
    path('student/marks/',views.GetMarks,name="get_student_marks"),
    path('student/marks/<int:pk>',views.getMark,name="getmark"),
    path('student/add-marks/<int:pk>',views.AddMarks,name="addmarks"),
#<--------------------------------student-Marks----------------------------->
    path('student/results/',views.getResult,name="results"),

    
]
