import django_filters
from users.models import Payment

class PaymentFilter(django_filters.FilterSet):
    """Фильтр для модели Payment."""

    course = django_filters.NumberFilter(field_name="course__id", lookup_expr="exact")
    lesson = django_filters.NumberFilter(field_name="lesson__id", lookup_expr="exact")
    payment_method = django_filters.ChoiceFilter(choices=Payment.PAYMENT_METHODS)
    ordering = django_filters.OrderingFilter(fields=["date"])

    class Meta:
        model = Payment
        fields = "__all__"
        # fields = ["course", "lesson", "payment_method"]
