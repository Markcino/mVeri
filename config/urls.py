
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('account/', include('accounts.urls')),
    path('superadmin/', include('superadmin.urls')),
    path('schooladmin/', include('schooladmin.urls')),
    path('student/', include('student.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
