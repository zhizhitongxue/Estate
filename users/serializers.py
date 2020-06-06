# _*_ coding:utf-8 _*_
__author__ = 'zhixin'
__date__ = '2020/6/6 9:28 AM'

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class IDSerializer(serializers.Serializer):
    ID = serializers.CharField(max_length=20, help_text='证件号码')
