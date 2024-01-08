from django.contrib import admin
from .models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'instructor',)
    list_display_links = ('id', 'title',)
    list_per_page = 10
    ordering = ['start_date', 'title',]
    list_filter = ('id', 'title', 'start_date', 'end_date', 'instructor',)
    search_fields = ('id', 'title', 'instructor__name',)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)
    list_display_links = ('id', 'name',)
    list_filter = ('id', 'name', 'email',)
    list_per_page = 10
    search_fields = ('id', 'name', 'email',)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'course',)
    list_display_links = ('id', 'title',)
    list_filter = ('id', 'title', 'course',)
    search_fields = ('id', 'title', 'course__title',)
    list_per_page = 10


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'content', 'module',)
    list_display_links = ('id', 'title',)
    list_filter = ('id', 'title', 'module',)
    list_per_page = 10
    search_fields = ('id', 'title', 'module__title',)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'enrollment_date', 'status',)
    list_display_links = ('id', 'user',)
    list_per_page = 10
    list_filter = ('id', 'user', 'course', 'enrollment_date', 'status',)
    search_fields = ('id', 'user__name', 'course__title', 'enrollment_date', 'status',)


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'module', 'progress', 'last_updated',)
    list_display_links = ('id', 'user',)
    list_per_page = 10
    list_filter = ('id', 'user', 'course', 'module', 'progress', 'last_updated',)
    search_fields = ('id', 'user__name', 'course__title', 'module__title', 'last_updated',)
