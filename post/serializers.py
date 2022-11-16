from rest_framework import serializers

from authentication.serializers import UserDetailSerializer

from .models import Media, Post


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user_data = serializers.SerializerMethodField('get_user_data', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'url',
            'content',
            'location',
            'location_str',
            'favorites_count',
            'date_created',
            'date_updated',
            'user',
            'user_data',
            'media',
        ]

    def get_user_data(self, obj):
        return UserDetailSerializer(obj.user, context=self.context).data
