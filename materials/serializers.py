from rest_framework import serializers
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Урок."""

    class Meta:
        """Мета класс для сериализатора."""

        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курс."""

    class Meta:
        """Мета класс для сериализатора."""

        lessons_count = serializers.SerializerMethodField()  # Количество уроков
        lessons = LessonSerializer(many=True, read_only=True)  # Уроки

        @staticmethod
        def get_lessons_count(obj):
            return obj.lessons.count()

        model = Course
        fields = "__all__"
