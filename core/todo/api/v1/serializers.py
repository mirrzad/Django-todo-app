from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.api.v1.serializers import UserSerializer
from ...models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'is_completed', 'created_time', 'updated_time']
        read_only_fields = ['user']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserSerializer(instance.user).data
        return rep

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = User.objects.get(id=request.user.id)
        return super().create(validated_data)


