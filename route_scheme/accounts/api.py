# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from accounts.serializers import (
    UserSerializer,
    SigninSerializer,
)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @list_route(methods=['GET'])
    def profile(self, request):
        return Response(self.get_serializer(request.user).data)

    @list_route(methods=['POST'], permission_classes=[AllowAny, ])
    def signin(self, request):
        serializer = SigninSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.data['username']
        password = serializer.data['password']

        user = get_object_or_404(User, username=username)
        user = authenticate(username=user.username, password=password)
        if user is None:
            error = _('The login and/or password you specified are not correct.')
            return Response({'error': error}, status=status.HTTP_401_UNAUTHORIZED)

        django_login(request, user)
        return Response({'next': '/'}, status=status.HTTP_302_FOUND)

    @list_route(methods=['GET'], permission_classes=[AllowAny, ])
    def logout(self, request):
        django_logout(request)
        return Response({'next': '/'}, status=status.HTTP_302_FOUND)
