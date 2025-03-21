from .views import JobListAPIView, PostCreateListAPIView, ApplicationCreateAPIView,CommentCreateListAPIView,UserApiView
# from .views import JobListAPIView, PostCreateListAPIView
from django.urls import path

urlpatterns = [
    path('jobs/', JobListAPIView.as_view(), name='jobs'),
    path('posts/', PostCreateListAPIView.as_view(), name='posts'),
    path('application/', ApplicationCreateAPIView.as_view(), name='applications'),
    path('post/comments/', CommentCreateListAPIView.as_view(), name ='comments'),
    path('user/profile/', UserApiView.as_view(), name ='userprofile'),
]