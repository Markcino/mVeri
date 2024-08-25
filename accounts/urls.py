from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('do_login', views.do_login, name="do_login"),
    path('register', views.register, name="register"),
    path('logout', views.do_logout, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
