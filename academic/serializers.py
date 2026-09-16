# Convierte los modelos a datos JSON.

from rest_framework import serializers

from .models import Course, Student, StudentCourse, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source='teacher', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'teacher_name']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name']


class StudentCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student', read_only=True)
    course = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = StudentCourse
        fields = ['id', 'student', 'student_name', 'course']