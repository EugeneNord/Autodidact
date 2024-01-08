from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('contacts/', show_contacts, name='contacts'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/<int:pk>/modules/', ModuleListView.as_view(), name='course_module'),
    path('course/<int:pk>/modules/<int:module_pk>/', MaterialListView.as_view(), name='material_detail'),
]
