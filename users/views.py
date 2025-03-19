from rest_framework import viewsets
from .models import User, Payment
from .serializers import UserSerializer, PaymentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Класс для представления пользователей в API."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """Класс для представления оплат в API."""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
