# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from mode.models import Mode
from mode.serializers import ModeSerializer


class ModeViewSet(viewsets.ModelViewSet):
    queryset = Mode.objects.all()
    serializer_class = ModeSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.request.user.mode_set.all() | Mode.objects.filter(user=None)
