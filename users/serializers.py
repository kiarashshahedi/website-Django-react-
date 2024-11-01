from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name', 'mobile', 'email', 'is_seller']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'mobile', 'password', 'is_seller']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser.objects.create_user(
            mobile=validated_data['mobile'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_seller=validated_data.get('is_seller', False)
        )
        return user

class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    password = serializers.CharField()
