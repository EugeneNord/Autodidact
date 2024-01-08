from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from django.views.generic import ListView, DetailView


def index(request):
    return render(request, 'autodidact/index.html')


def show_contacts(request):
    data = {
        'title': 'Контакты',
    }
    return render(request, 'autodidact/contacts.html', data)


class CourseListView(ListView):
    model = Course
    template_name = 'autodidact/course_list.html'
    ordering = ['start_date']


class CourseDetailView(DetailView):
    model = Course
    template_name = 'autodidact/course_detail.html'
    context_object_name = 'course'


class ModuleListView(ListView):
    model = Module
    template_name = 'autodidact/course_module.html'
    context_object_name = 'module'

    def get_queryset(self):
        return Module.objects.filter(course__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(pk=self.kwargs['pk'])
        return context


class MaterialListView(ListView):
    model = Material
    template_name = 'autodidact/material_detail.html'
    context_object_name = 'material'

    def get_queryset(self):
        return Material.objects.filter(module__id=self.kwargs['module_pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['module'] = Module.objects.get(pk=self.kwargs['module_pk'])
        return context
