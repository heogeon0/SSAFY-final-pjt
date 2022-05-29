from distutils.errors import CompileError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Review
from .comment import CommentSerializer

User = get_user_model()

# Review Create/Detail/Update
class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta: 
            model = User
            fields = ('username', )
    
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    
    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'content', 'created_at', 'updated_at', 'comments', 'like_count', 'kind',)

class ReviewListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('username', )
    user = UserSerializer(read_only=True)
    like_count = serializers.IntegerField()
    comment_count = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ('pk', 'user', 'title', 'created_at', 'like_count', 'comment_count', 'kind')