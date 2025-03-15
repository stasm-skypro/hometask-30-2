from rest_framework import serializers
from .models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курс."""

    lessons_count = serializers.SerializerMethodField()

    @staticmethod
    def get_lessons_count(obj):
        """Получение количества уроков в курсе."""
        return obj.lessons.count()


    class Meta:
        """Мета класс для сериализатора."""

        model = Course
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Урок."""

    class Meta:
        """Мета класс для сериализатора."""

        model = Lesson
        fields = "__all__"
