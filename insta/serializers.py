from rest_framework import serializers

from .models import Post, Profile


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = ['id','follower']
