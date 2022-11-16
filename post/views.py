from rest_framework import permissions, viewsets

from .models import Media, Post
from .serializers import MediaSerializer, PostSerializer


class MediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint for media files information
    """

    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for posts
    """

    queryset = Post.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
