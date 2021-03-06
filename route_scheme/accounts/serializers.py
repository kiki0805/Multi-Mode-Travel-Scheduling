# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from accounts.models import UserProfile
from tags.serializers import TagSerializer
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    tags = TagSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'tags', 'location_count')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')


class SigninSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
