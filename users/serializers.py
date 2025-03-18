from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User."""
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "is_staff", "is_active", "date_joined"]
        read_only_fields = ["id", "is_staff", "is_active", "date_joined"]  # Дополнительно определяем поля, которые нельзя изменять
        extra_kwargs = {  # Дополнительные настройки для полей, которые позволяют, например, делать их обязательными, или только для чтения, или скрытыми
            "username": {"required": False},
            "email": {"required": True},
        }
