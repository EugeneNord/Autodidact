from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'instructor',)
    list_filter = ('id', 'title', 'start_date', 'end_date', 'instructor',)
    search_fields = ('id', 'title', 'instructor__name',)


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',)
    list_filter = ('id', 'name', 'email',)
    search_fields = ('id', 'name', 'email',)


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'course',)
    list_filter = ('id', 'title', 'course',)
    search_fields = ('id', 'title', 'course__title',)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'content', 'module',)
    list_filter = ('id', 'title', 'module',)
    search_fields = ('id', 'title', 'module__title',)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'enrollment_date', 'status',)
    list_filter = ('id', 'user', 'course', 'enrollment_date', 'status',)
    search_fields = ('id', 'user__name', 'course__title', 'enrollment_date', 'status',)


class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'module', 'progress', 'last_updated',)
    list_filter = ('id', 'user', 'course', 'module', 'progress', 'last_updated',)
    search_fields = ('id', 'user__name', 'course__title', 'module__title', 'last_updated',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(UserProgress, UserProgressAdmin)
