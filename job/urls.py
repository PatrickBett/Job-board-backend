from .views import JobListAPIView, PostCreateListAPIView, ApplicationCreateAPIView,CommentCreateListAPIView,UserApiView,UserProfileViewSet, SkillViewSet, LanguageViewSet, EducationViewSet
# from .views import JobListAPIView, PostCreateListAPIView
from django.urls import path,include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet, basename='profile')
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'languages', LanguageViewSet, basename='language')
router.register(r'education', EducationViewSet, basename='education')


urlpatterns = [
    path('jobs/', JobListAPIView.as_view(), name='jobs'),
    path('posts/', PostCreateListAPIView.as_view(), name='posts'),
    path('application/', ApplicationCreateAPIView.as_view(), name='applications'),
    path('post/comments/', CommentCreateListAPIView.as_view(), name ='comments'),
    path('user/profile/', UserApiView.as_view(), name ='userprofile'),
    path('user/', include(router.urls)),
]