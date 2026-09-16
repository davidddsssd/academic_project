# Define las rutas de paginas y API.

from django.urls import path
from django.views.generic import RedirectView

from .views import (
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
    CourseStudentListCreateAPIView,
    CourseStudentRetrieveDestroyAPIView,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView,
    TeacherListCreateAPIView,
    TeacherRetrieveUpdateDestroyAPIView,
    TeacherCoursesListAPIView,
    courses_page,
    api_home,
    students_page,
    teachers_page,
    course_students_page,
    teacher_courses_page,
)

app_name = 'academic'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='academic:courses', permanent=False), name='home'),
    path('courses/', courses_page, name='courses'),
    path('students/', students_page, name='students'),
    path('teachers/', teachers_page, name='teachers'),
    path('api/', api_home, name='api-home'),
    path('courses/<int:course_id>/students/', course_students_page, name='course-students'),
    path('teachers/<int:teacher_id>/courses/', teacher_courses_page, name='teacher-courses'),
    path('api/courses/', CourseListCreateAPIView.as_view(), name='api-courses'),
    path('api/courses/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='api-course-detail'),
    path('api/students/', StudentListCreateAPIView.as_view(), name='api-students'),
    path('api/students/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='api-student-detail'),
    path('api/teachers/', TeacherListCreateAPIView.as_view(), name='api-teachers'),
    path('api/teachers/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name='api-teacher-detail'),
    path('api/teachers/<int:teacher_id>/courses/', TeacherCoursesListAPIView.as_view(), name='api-teacher-courses'),
    path('api/courses/<int:course_id>/students/', CourseStudentListCreateAPIView.as_view(), name='api-course-students'),
    path('api/courses/<int:course_id>/students/<int:pk>/', CourseStudentRetrieveDestroyAPIView.as_view(), name='api-course-student-detail'),
]