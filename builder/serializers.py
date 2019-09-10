from rest_framework import serializers


class MenuSerializer(serializers.Serializer):
    menu = serializers.CharField()