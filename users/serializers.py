from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "password", "confirm_password")

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.pop("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

        # Validate the password using Django's password validators
        try:
            validate_password(password, self.instance)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(e)

        return data

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )
