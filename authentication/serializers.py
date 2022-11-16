from django.contrib.auth.models import User
from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'first_name',
            'last_name',
            'name',
            'bio',
            'image',
            'phone',
            'email',
            'location',
            'date_birth',
            'date_joined',
            'last_login',
            'is_staff',
            'is_active',
            'is_superuser',
            'date_created',
            'date_updated',
        ]


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'first_name',
            'last_name',
            'name',
            'bio',
            'image',
            'phone',
            'email',
            'location',
            'date_birth',
            'date_joined',
            'last_login',
            'is_staff',
            'is_active',
            'is_superuser',
            'date_created',
            'date_updated',
        ]
