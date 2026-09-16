# Define las tablas y datos del sistema.

from django.db import models


class Teacher(models.Model):
	"""Datos del profesor."""

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	class Meta:
		ordering = ['last_name', 'first_name']

	def __str__(self):
		return f'{self.first_name} {self.last_name}'


class Course(models.Model):
	"""Datos del curso."""

	name = models.CharField(max_length=150)
	teacher = models.ForeignKey(
		Teacher,
		on_delete=models.PROTECT,
		related_name='courses',
	)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Student(models.Model):
	"""Datos del estudiante."""

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	class Meta:
		ordering = ['last_name', 'first_name']

	def __str__(self):
		return f'{self.first_name} {self.last_name}'


class StudentCourse(models.Model):
	"""Inscripción del estudiante."""

	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	class Meta:
		constraints = [
			models.UniqueConstraint(
				fields=['student', 'course'],
				name='unique_student_course',
			),
		]

	def __str__(self):
		return f'{self.student} - {self.course}'
