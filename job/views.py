from .models import Job,Post, Application,Comment
from .models import Job,Post
# from .serializer import JobSerializer, UserSerializer, PostSerializer
from .serializer import JobSerializer, UserSerializer, PostSerializer, ApplicationSerializer,CommentSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class JobListAPIView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    

    # def get_queryset(self):
    #     user = self.request.user
    #     return Job.objects.filter(author = user)
  

class UserCreateAPIView (generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class PostCreateListAPIView (generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class ApplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    queryset = Application.objects.all()

class CommentCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')  # Get post ID from the request
        post = Post.objects.get(id=post_id)  # Retrieve the post
        serializer.save(post = post, user = self.request.user)

class UserApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user

        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        })