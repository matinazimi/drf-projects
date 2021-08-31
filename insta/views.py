from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, generics, filters

from .models import Post, Profile
from .serializers import PostSerializer, ProfileSerializer


class PostView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['profile', ]
    search_fields = ['caption', ]

    def get_queryset(self):
        queryset = Post.objects.filter(profile__user__id=self.request.user.id)
        return queryset


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
