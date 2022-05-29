from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import Comment

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    user = UserSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = ('pk', 'user', 'content', 'like_count')