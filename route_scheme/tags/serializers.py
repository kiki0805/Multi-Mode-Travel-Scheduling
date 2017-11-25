# -*- coding: utf-8 -*-
from tags.models import Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')

    def create(self, validated_data):
        user = self.context['request'].user
        title = validated_data['title']
        tag = Tag.objects.create(title=title)
        user.profile.tags.add(tag)
        return tag
