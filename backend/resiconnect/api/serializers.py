from rest_framework import serializers
from .models import Apartment, Resident, Post


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


# Serializer for the Resident model with detailed apartment information
class ResidentDetailSerializer(serializers.ModelSerializer):
    apartment = ApartmentSerializer()

    class Meta:
        model = Resident
        fields = '__all__'


# Serializer for the Post model with detailed resident information
class PostDetailSerializer(serializers.ModelSerializer):
    resident = ResidentDetailSerializer()

    class Meta:
        model = Post
        fields = '__all__'


# Serializer for the Resident model for writing operations
class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = '__all__'


# Serializer for the Post model for writing operations
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
