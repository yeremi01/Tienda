from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Tienda.views import login, Productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login),
    path('Productos/',Productos),
]

if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
