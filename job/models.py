from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    budget = models.FloatField()
    location = models.CharField(max_length= 50,default="Nairobi")
    company = models.CharField(max_length=30, default="Safaricom")
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
class Post(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE,  related_name="posts")
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:20]
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE,  related_name="comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    
    comment = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment[:20]
    
class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="jobs")
    cv = models.FileField(upload_to='cv/')
    resume = models.FileField(upload_to='resume/')
    cover_letter = models.FileField(upload_to='cover/')
    aob = models.TextField(max_length=500)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='skills')
    proficiency = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert')
    ])
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='languages')
    proficiency = models.CharField(max_length=20, choices=[
        ('basic', 'Basic'),
        ('conversational', 'Conversational'),
        ('fluent', 'Fluent'),
        ('native', 'Native')
    ])
    
    def __str__(self):
        return self.name

class Education(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.degree} from {self.institution}"
    
class Review(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE,  related_name="reviews")
    review = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.review