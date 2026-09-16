# Controla las paginas y respuestas de la API.

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.db.models.deletion import ProtectedError

from rest_framework import generics, serializers

from .models import Course, Student, StudentCourse, Teacher
from .serializers import (
	CourseSerializer,
	StudentCourseSerializer,
	StudentSerializer,
	TeacherSerializer,
)


def courses_page(request):
	"""Muestra los cursos."""
	return render(request, 'academic/courses.html')


def students_page(request):
	"""Muestra los estudiantes."""
	return render(request, 'academic/students.html')


def teachers_page(request):
	"""Muestra los profesores."""
	return render(request, 'academic/teachers.html')


def api_home(request):
	"""Muestra las rutas de la API."""
	return JsonResponse({
		'courses': '/api/courses/',
		'students': '/api/students/',
		'teachers': '/api/teachers/',
	})


def teacher_courses_page(request, teacher_id):
	"""Muestra los cursos del profesor."""
	teacher = get_object_or_404(Teacher, id=teacher_id)
	return render(request, 'academic/teacher_courses.html', {'teacher': teacher})


def course_students_page(request, course_id):
	"""Muestra los estudiantes del curso."""
	course = get_object_or_404(Course.objects.select_related('teacher'), id=course_id)
	return render(request, 'academic/course_students.html', {'course': course})


class CourseListCreateAPIView(generics.ListCreateAPIView):
	queryset = Course.objects.select_related('teacher').all()
	serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Course.objects.select_related('teacher').all()
	serializer_class = CourseSerializer


class StudentListCreateAPIView(generics.ListCreateAPIView):
	"""Lista y crea estudiantes."""

	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer


class TeacherListCreateAPIView(generics.ListCreateAPIView):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer


class TeacherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer

	def perform_destroy(self, instance):
		try:
			instance.delete()
		except ProtectedError as error:
			raise serializers.ValidationError(
				{'detail': 'No se puede eliminar un profesor que tiene cursos asignados.'}
			) from error


class TeacherCoursesListAPIView(generics.ListAPIView):
	"""Lista cursos de un profesor."""

	serializer_class = CourseSerializer

	def get_queryset(self):
		return Course.objects.select_related('teacher').filter(
			teacher_id=self.kwargs['teacher_id']
		)


class CourseStudentListCreateAPIView(generics.ListCreateAPIView):
	"""Lista y registra estudiantes."""

	serializer_class = StudentCourseSerializer

	def get_queryset(self):
		return StudentCourse.objects.select_related('student', 'course').filter(
			course_id=self.kwargs['course_id']
		)

	def perform_create(self, serializer):
		serializer.save(course_id=self.kwargs['course_id'])


class CourseStudentRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
	serializer_class = StudentCourseSerializer

	def get_queryset(self):
		return StudentCourse.objects.select_related('student', 'course').filter(
			course_id=self.kwargs['course_id']
		)
