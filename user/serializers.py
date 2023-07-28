from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import AuthUser


class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuthUser
        fields = ('id', 'username', 'first_name',
                  'last_name', 'role', 'email', 'password')
        read_only_fields = ('username', 'email')


class RegisterAuthUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=AuthUser.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = AuthUser
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'role')

    def create(self, validated_data):

        role = validated_data['role']

        is_staff = False

        if (role == 'admin'):
            is_staff = True
            is_superuser = True

        user = AuthUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=role,
            is_staff=is_staff,
            is_superuser=is_superuser
        )

        user.set_password(validated_data['password'])

        user.save()

        return user
