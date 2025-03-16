from rest_framework import serializers

from users.models import Payment
from users.serializers import UserSerializer
from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Урок."""

    class Meta:
        """Мета класс для сериализатора."""
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Курс."""

    lessons_count = serializers.SerializerMethodField()  # Количество уроков
    lessons = LessonSerializer(many=True, read_only=True)  # Уроки

    @staticmethod
    def get_lessons_count(obj):
        """Получение количества уроков в курсе."""
        return obj.lessons.count()


    class Meta:
        """Мета класс для сериализатора."""

        model = Course
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Платеж."""

    user = UserSerializer(read_only=True)  # Вложенный сериализатор пользователя
    course = CourseSerializer(read_only=True)  # Вложенный сериализатор курса
    lesson = LessonSerializer(read_only=True)  # Вложенный сериализатор урока
    payment_method = serializers.ChoiceField(
        choices=Payment.PAYMENT_METHODS
    )  # Вывод доступных методов оплаты

    class Meta:
        model = Payment
        fields = "__all__"
        # fields = ["id", "user", "date", "course", "lesson", "amount", "payment_method"]
