from rest_framework import serializers
from chat.models import * 
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ['password', 'last_login', 'date_joined', 'slug', 'has_profile', 'remember_me']


class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150)
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'
    
    def get_user(self, obj):
        user = obj.user
        serializer = UserSerializer(user,  many=False)
        return serializer.data

        