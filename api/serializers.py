from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'phone', 'image', 'date_creation', 'updated_on')


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'profile')
        extra_kwargs = {'password': {"write_only": True, 'required': True}}

    def create(self, validated_data):
        user_profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **user_profile_data)
        return user
