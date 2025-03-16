from users.apps import UsersConfig
from rest_framework import routers
from .views import UserViewSet

app_name = UsersConfig.name

routers = routers.DefaultRouter()
routers.register(r"user", UserViewSet, basename="user")
routers.register(r"payment", UserViewSet, basename="payment")

urlpatterns = routers.urls
