from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'first_name', 'family_name', 'age', 'gender',
            'address', 'postal_code', 'meli_card_number', 'user_type', 'store_name', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data.get('user_type') == 'seller' and not data.get('store_name'):
            raise serializers.ValidationError("Store name is required for sellers.")
        return data

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            family_name=validated_data.get('family_name', ''),
            age=validated_data.get('age', None),
            gender=validated_data.get('gender', ''),
            address=validated_data.get('address', ''),
            postal_code=validated_data.get('postal_code', ''),
            meli_card_number=validated_data.get('meli_card_number', ''),
            user_type=validated_data.get('user_type', CustomUser.BUYER),
            store_name=validated_data.get('store_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        return super().update(instance, validated_data)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'family_name': self.user.family_name,
            'age': self.user.age,
            'gender': self.user.gender,
            'address': self.user.address,
            'postal_code': self.user.postal_code,
            'meli_card_number': self.user.meli_card_number,
            'user_type': self.user.user_type,
            'store_name': self.user.store_name,
        })
        return data


