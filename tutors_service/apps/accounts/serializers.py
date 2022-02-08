from rest_framework import serializers
from tutors_service.apps.accounts.models.user_account import UserAccount
from django.contrib.auth import authenticate

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("uuid", "email", "first_name", "last_name")


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ("uuid", "email", "password", "first_name", "last_name")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserAccount.objects.create_user(
            password=validated_data["password"],
            email=validated_data["email"],
            first_name=validated_data["last_name"],
            last_name=validated_data["last_name"],
        )

        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
