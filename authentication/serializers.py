from rest_framework import serializers
from .models import MyUser
from rest_framework.validators import UniqueValidator

class UserRegisterSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True, max_length=100,min_length=6,validators=[UniqueValidator(queryset=MyUser.objects.all())])
    password=serializers.CharField(write_only=True,required=True, max_length=100,min_length=6)
    first_name=serializers.CharField(required=False)
    last_name=serializers.CharField(required=False)
    created = serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return MyUser.objects.create_user(**validated_data)