# apps/authentication/serializers.py
from djoser.serializers import UserCreateSerializer as BaseCreateSerializer, UserSerializer as BaseUserSerializer
from .models import User

class UserCreateSerializer(BaseCreateSerializer):
    class Meta(BaseCreateSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'username', 'password', 're_password',
            'first_name', 'last_name', 'phone_number', 'address',
            'date_of_birth', 'gender', 'profile_picture'
        )

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'username', 'first_name', 'last_name',
            'phone_number', 'address', 'date_of_birth',
            'gender', 'is_verified', 'profile_picture'
        )
