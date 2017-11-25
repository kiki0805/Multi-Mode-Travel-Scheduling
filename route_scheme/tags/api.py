# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from tags.models import Tag
from tags.serializers import TagSerializer
from tags.service import TagService


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Tag.objects.all()

    @list_route(methods=['GET'])
    def assign(self, request):
        TagService.get_related_tags(request.user)
        return Response(status=status.HTTP_200_OK)
