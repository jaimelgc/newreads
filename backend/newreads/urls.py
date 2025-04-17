from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
    path('user/', include('userprofile.urls')),
    path('forum/', include('forum.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
