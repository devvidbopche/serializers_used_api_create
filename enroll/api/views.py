from enroll.models import User
from enroll.api.serializer import UserViewSet
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework. permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserViewSet

authentication_classes = [SessionAuthentication,]
permission_classes = [IsAuthenticated]