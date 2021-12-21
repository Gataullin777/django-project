from django.contrib import admin

from students.models import Course, Student


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ["id", "name"]



@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ["id", "name", "birth_date"]