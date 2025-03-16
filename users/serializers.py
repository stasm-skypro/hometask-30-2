from rest_framework import serializers

from materials.serializers import CourseSerializer, LessonSerializer
from users.models import User, Payment


# Для дополнительного задания перенес из файла materials/serializers.py
class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Платеж."""

    course = CourseSerializer(read_only=True)  # Вложенный сериализатор курса
    lesson = LessonSerializer(read_only=True)  # Вложенный сериализатор урока
    payment_method = serializers.ChoiceField(
        choices=Payment.PAYMENT_METHODS
    )  # Вывод доступных методов оплаты

    class Meta:
        model = Payment
        fields = "__all__"
        

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    # payments = PaymentSerializer(many=True, read_only=True, source="payments")
    payments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined", "payments"
        ]

        # Дополнительно определяем поля, которые нельзя изменять
        read_only_fields = ["id", "is_staff", "is_active", "date_joined"]

        # Дополнительные настройки для полей, которые позволяют, например, делать их обязательными, или только
        # для чтения, или скрытыми
        extra_kwargs = {
            "username": {"required": False},
            "email": {"required": True},
        }
