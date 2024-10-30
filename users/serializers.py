# users/serializers.py

from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user and for user profile.
    """
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'first_name', 'family_name', 'age', 'gender',
            'address', 'postal_code', 'meli_card_number', 'user_type', 'store_name', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Override the create method to handle password hashing.
        """
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
            additional_info=validated_data.get('additional_info', ''),
            user_type=validated_data.get('user_type', CustomUser.BUYER),  # Default to BUYER if not specified
            store_name=validated_data.get('store_name', '')  # Ensure store_name is optional
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Override update to handle password change securely if provided.
        """
        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))
        return super().update(instance, validated_data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer for JWT token login, adding extra user information to the response.
    """
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
            'additional_info': self.user.additional_info,
            'user_type': self.user.user_type,  # Include user_type in the response
            'store_name': self.user.store_name,  # Include store_name if applicable
        })
        return data

class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for handling password change.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        """
        Validate new password using Django's default password validation.
        """
        validate_password(value)
        return value
