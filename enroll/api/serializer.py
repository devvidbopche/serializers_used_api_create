from enroll.models import User
from rest_framework import serializers


class UserViewSet(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']


