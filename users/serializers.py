from rest_framework import serializers
from .models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Payment."""

    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined"
        ]

        # Дополнительно определяем поля, которые нельзя изменять
        read_only_fields = [
            "id", "is_staff", "is_active", "date_joined"
        ]

        # Дополнительные настройки для полей, которые позволяют, например, делать их обязательными, или только для чтения, или скрытыми
        extra_kwargs = {
            "username": {"required": False},
            "email": {"required": True},
        }
