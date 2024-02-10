from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from users.serializers import UserRegistrationSerializer, UserLoginSerializer


class UserRegistrationApiView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserRegistrationSerializer


class UserLoginApiView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response({"detail": "Invalid credentials"}, status=401)
