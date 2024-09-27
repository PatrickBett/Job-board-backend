from rest_framework import serializers
from .models import Job,Post,Comment,Application
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","first_name","last_name","password"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class PostSerializer(serializers.ModelSerializer):
     user = UserSerializer(read_only=True)
     class Meta:
        model = Post
        fields = ["id","user","content","time"]
        extra_kwargs = {"user":{"read_only":True}}

class ApplicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)
    class Meta:
        model = Application
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    post = PostSerializer(read_only = True)
    class Meta:
        model = Comment
        fields ="__all__"