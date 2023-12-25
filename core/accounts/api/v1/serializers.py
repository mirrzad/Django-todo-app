from rest_framework import serializers
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core import exceptions


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
        fields = ['username', 'full_name']


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password1']

    def validate(self, attrs):
        password = attrs.get('password')
        password1 = attrs.get('password1')

        if password != password1:
            raise serializers.ValidationError({"detail": "passwords doesn't match!"})
        try:
            password_validation.validate_password(password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})

        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('password1', None)
        return super().create(validated_data)
