from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.show_contacts, name='contacts'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/<int:pk>/modules/', views.ModuleListView.as_view(), name='course_module'),
    path('course/<int:pk>/modules/<int:module_pk>/', views.MaterialListView.as_view(), name='material_detail'),
]
