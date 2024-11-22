from django.contrib import admin
from django.urls import path, include
urlpatterns = [
 path('', include('core.urls')),
 path('services/', include('services.urls')),
 path('admin/', admin.site.urls),
]

from django.conf import settings
if settings.DEBUG:
 from django.conf.urls.static import static
 urlpatterns += static(settings.MEDIA_URL,
 document_root=settings.MEDIA_ROOT)

