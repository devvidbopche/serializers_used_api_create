from enroll.models import User
from enroll.api.serializer import UserViewSet

from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserViewSet