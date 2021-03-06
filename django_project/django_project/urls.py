from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('dialogs.urls')),
    path('', include('users.urls')),
    path('', include('base.urls')),
    path('', include('friends.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
