from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('library/', include('library.urls')),
    path('user/', include('userprofile.urls')),
    path('forum/', include('forum.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
