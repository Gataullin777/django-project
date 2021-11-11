from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    # ordering = Student.objects.order_by('group')
    ordering = Student.objects.order_by('name').prefetch_related('teacher')
    context = {'data': ordering}
    return render(request, template, context)
