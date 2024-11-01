
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from job.views import UserCreateAPIView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/",UserCreateAPIView.as_view(),name = 'register'),
    path("api/token/", TokenObtainPairView.as_view(),name = "get-token"),
    path("api/token/refresh/",TokenRefreshView.as_view(), name = "refresh"),
    path("api-auth/",include("rest_framework.urls")),
    path('api/', include('job.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
