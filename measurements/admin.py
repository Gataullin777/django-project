from django.contrib import admin
from .models import Project, Measurement



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Проект'
        verbose_name_prupal = 'Проекты'

    list_display = ['name', 'latitude', 'longitude', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']



@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Измерение'
        verbose_name_prupal = 'Измерения'


    list_display = ['value', 'project', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']




