# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from mode.models import Mode
from rest_framework import serializers
import json



class ModeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    duration = serializers.SerializerMethodField()
    begin_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()
    come_over_locations = serializers.SerializerMethodField()

    class Meta:
        model = Mode
        fields = ('id', 'name', 'username', 'duration', 'begin_time', 'end_time', 'come_over_locations')

    def create(self, validated_data):
        user = self.context['request'].user
        name = validated_data['name']
        duration = validated_data['duration']
        begin_time = validated_data['begin_time']
        end_time = validated_data['end_time']
        come_over_locations = validated_data['come_over_locations']
        extra_fields = {}
        extra_fields['duration'] = duration
        extra_fields['begin_time'] = begin_time
        extra_fields['end_time'] = end_time
        extra_fields['come_over_locations'] = come_over_locations
        mode = Mode.objects.create(user=user, name=name, extra_fields=extra_fields)
        return mode

    def get_duration(self, obj):
        extra_fields = obj.extra_fields
        return extra_fields['duration']

    def get_begin_time(self, obj):
        extra_fields = obj.extra_fields
        return extra_fields['begin_time']

    def get_end_time(self, obj):
        extra_fields = obj.extra_fields
        return extra_fields['end_time']

    def get_come_over_locations(self, obj):
        extra_fields = obj.extra_fields
        return extra_fields['come_over_locations']
