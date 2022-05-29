from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Score

User = get_user_model()


class ScoreSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    user = UserSerializer(read_only = True)
    class Meta:
        model = Score
        fields = ('pk', 'number', 'content', 'user',)
