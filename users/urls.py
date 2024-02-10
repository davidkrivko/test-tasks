from django.urls import path

from users.views import UserRegistrationApiView, UserLoginApiView


urlpatterns = [
    path("registration/", UserRegistrationApiView.as_view(), name="register"),
    path("login/", UserLoginApiView.as_view(), name="register"),
]

app_name = "users"
