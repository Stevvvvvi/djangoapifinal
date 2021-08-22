from rest_framework import serializers
from .models import MyUser
from rest_framework.validators import UniqueValidator

class UserRegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True, max_length=100,min_length=6,validators=[UniqueValidator(queryset=MyUser.objects.all())])
    password=serializers.CharField(write_only=True,required=True, max_length=100,min_length=6)
    # first_name=serializers.CharField(required=False)
    # last_name=serializers.CharField(required=False)


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return MyUser.objects.create_user(**validated_data)

    class Meta:
        model = MyUser
        fields = ['email','password','first_name','last_name','id','modified', 'created']
        read_only_fields = ['id','modified', 'created']

class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True, max_length=100,min_length=6,validators=[UniqueValidator(queryset=MyUser.objects.all())])
    password=serializers.CharField(write_only=True,required=True, max_length=100,min_length=6)
    token_type = serializers.ReadOnlyField(default='Bearer')

    class Meta:
        model = MyUser
        fields = ['email','password' ,'id','modified', 'created','token_type','last_login', 'token']
        read_only_fields = ['id','modified', 'created','token_type', 'last_login','token']

