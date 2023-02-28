from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import UserProfile, Tags, Posts


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'phone', 'image', 'date_create', 'date_update')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'profile')
        extra_kwargs = {'password': {"write_only": True, 'required': True}}

    def create(self, validated_data):
        user_profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user = user, **user_profile_data)
        return user


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'name')


class PostsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer()

    class Meta:
        model = Posts
        fields = ('id', 'title', 'content', 'image', 'tags', 'author', 'views_count', 'date_create', 'date_update')
