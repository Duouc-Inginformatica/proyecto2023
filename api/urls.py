from django.urls import path #importar libreria path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import SebeViews #importar clase MauleViews

urlpatterns = [
    path('Datos/', SebeViews.as_view(), name='Datos_list'), #crear ruta index2
    path('Datos/<int:tipo>', SebeViews.as_view(), name='companies_process')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
