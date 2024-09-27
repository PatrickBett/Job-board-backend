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
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User,on_delete= models.CASCADE,  related_name="comment")
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
