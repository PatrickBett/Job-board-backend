from rest_framework import serializers
from .models import Job,Post,Comment,Application,UserProfile, Skill, Language, Education
# from .models import Job,Post
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
        fields = fields = ["id", "user", "post", "comment", "time"]    


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'proficiency']
        read_only_fields = ['id']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name', 'proficiency']
        read_only_fields = ['id']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'current']
        read_only_fields = ['id']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'bio', 'location', 'birth_date', 'profile_picture', 'skills', 'languages', 'education','user']
        # read_only_fields = ['id']
