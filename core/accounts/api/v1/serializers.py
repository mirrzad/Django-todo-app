from rest_framework import serializers
from django.contrib.auth.models import  User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
        fields = ['username', 'full_name']
