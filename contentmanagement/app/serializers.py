# cms_app/serializers.py
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, Content, Category

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'full_name', 'first_name', 'last_name', 'role', 'phone', 
                  'address', 'city', 'state', 'country', 'pincode']

    def validate_password(self, value):
        if not any(c.isupper() for c in value) or not any(c.islower() for c in value) or len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters with 1 uppercase and 1 lowercase letter.")
        return value

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data.get('username', validated_data['email']),
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role'],
            phone=validated_data['phone'],
            pincode=validated_data['pincode'],
            address=validated_data.get('address', ''),
            city=validated_data.get('city', ''),
            state=validated_data.get('state', ''),
            country=validated_data.get('country', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ContentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Show author's name
    categories = CategorySerializer(many=True)

    class Meta:
        model = Content
        fields = ['id', 'title', 'body', 'summary', 'document', 'categories', 'author']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        content = Content.objects.create(**validated_data)
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(name=category_data['name'])
            content.categories.add(category)
        return content
