from materials.apps import MaterialsConfig
from rest_framework import routers
from .views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    PaymentViewSet,
)
from django.urls import path


app_name = MaterialsConfig.name


# URL-ы для Вьюсетов
router = routers.DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")
router.register(r"payment", PaymentViewSet, basename="payment")

# URL-ы для APIView
urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson-create"),
    path("lesson/list/", LessonListAPIView.as_view(), name="lesson-list"),
    path("lesson/list/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson-detail"),
    path("lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson-update"),
    path("lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson-delete"),
] + router.urls
